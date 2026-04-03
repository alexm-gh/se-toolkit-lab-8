"""VictoriaLogs and VictoriaTraces client."""

from __future__ import annotations

import json

import httpx


class ObsClient:
    """Client for VictoriaLogs and VictoriaTraces APIs."""

    def __init__(
        self,
        victorialogs_url: str,
        victoriatraces_url: str,
    ) -> None:
        self.victorialogs_url = victorialogs_url.rstrip("/")
        self.victoriatraces_url = victoriatraces_url.rstrip("/")
        self._http = httpx.AsyncClient(timeout=30.0)

    async def close(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> ObsClient:
        return self

    async def __aexit__(self, *args) -> None:
        await self.close()

    @staticmethod
    def _parse_ndjson(text: str) -> list[dict]:
        """Parse newline-delimited JSON (VictoriaLogs format)."""
        results = []
        for line in text.strip().splitlines():
            line = line.strip()
            if line:
                try:
                    results.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        return results

    # VictoriaLogs methods

    async def logs_search(
        self,
        query: str,
        limit: int = 100,
        time_range: str = "10m",
    ) -> list[dict]:
        """Search logs using LogsQL query.

        Args:
            query: LogsQL query string (e.g., 'severity:ERROR service.name:"backend"')
            limit: Max results to return
            time_range: Time range like '10m', '1h', '24h'
        """
        url = f"{self.victorialogs_url}/select/logsql/query"
        full_query = f"_time:{time_range} {query}"
        params = {"query": full_query, "limit": limit}
        response = await self._http.get(url, params=params)
        response.raise_for_status()
        return self._parse_ndjson(response.text)

    async def logs_error_count(
        self,
        service: str | None = None,
        time_range: str = "1h",
    ) -> dict:
        """Count errors by service over a time window."""
        url = f"{self.victorialogs_url}/select/logsql/query"
        query = f"_time:{time_range} severity:ERROR"
        if service:
            query += f' service.name:"{service}"'
        params = {"query": query, "limit": 1000}
        response = await self._http.get(url, params=params)
        response.raise_for_status()
        data = self._parse_ndjson(response.text)
        return {"count": len(data), "time_range": time_range, "service": service}

    # VictoriaTraces methods

    async def traces_list(
        self,
        service: str | None = None,
        limit: int = 20,
    ) -> list[dict]:
        """List recent traces for a service."""
        url = f"{self.victoriatraces_url}/select/jaeger/api/traces"
        params = {"limit": limit}
        if service:
            params["service"] = service
        response = await self._http.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])

    async def traces_get(self, trace_id: str) -> dict:
        """Fetch a specific trace by ID."""
        url = f"{self.victoriatraces_url}/select/jaeger/api/traces/{trace_id}"
        response = await self._http.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("data", {})
