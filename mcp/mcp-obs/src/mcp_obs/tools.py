"""Tool schemas, handlers, and registry for the MCP observability server."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from dataclasses import dataclass

from mcp.types import Tool
from pydantic import BaseModel, Field

from mcp_obs.client import ObsClient


class LogsSearchArgs(BaseModel):
    query: str = Field(
        description="LogsQL query (e.g., 'severity:ERROR service.name:\"backend\"')"
    )
    limit: int = Field(default=100, ge=1, le=1000, description="Max results")
    time_range: str = Field(
        default="10m",
        description="Time range like '10m', '1h', '24h'",
    )


class LogsErrorCountArgs(BaseModel):
    service: str | None = Field(
        default=None,
        description="Service name to filter (e.g., 'Learning Management Service')",
    )
    time_range: str = Field(
        default="1h",
        description="Time window like '10m', '1h', '24h'",
    )


class TracesListArgs(BaseModel):
    service: str | None = Field(
        default=None,
        description="Service name to filter traces",
    )
    limit: int = Field(default=20, ge=1, le=100, description="Max traces")


class TracesGetArgs(BaseModel):
    trace_id: str = Field(description="Trace ID to fetch")


ToolPayload = BaseModel | list | dict
ToolHandler = Callable[[ObsClient, BaseModel], Awaitable[ToolPayload]]


@dataclass(frozen=True, slots=True)
class ToolSpec:
    name: str
    description: str
    model: type[BaseModel]
    handler: ToolHandler

    def as_tool(self) -> Tool:
        schema = self.model.model_json_schema()
        schema.pop("$defs", None)
        schema.pop("title", None)
        return Tool(name=self.name, description=self.description, inputSchema=schema)


async def _logs_search(client: ObsClient, args: BaseModel) -> ToolPayload:
    a = args if isinstance(args, LogsSearchArgs) else LogsSearchArgs.model_validate(
        args.model_dump()
    )
    return await client.logs_search(a.query, a.limit, a.time_range)


async def _logs_error_count(client: ObsClient, args: BaseModel) -> ToolPayload:
    a = (
        args
        if isinstance(args, LogsErrorCountArgs)
        else LogsErrorCountArgs.model_validate(args.model_dump())
    )
    return await client.logs_error_count(a.service, a.time_range)


async def _traces_list(client: ObsClient, args: BaseModel) -> ToolPayload:
    a = (
        args
        if isinstance(args, TracesListArgs)
        else TracesListArgs.model_validate(args.model_dump())
    )
    return await client.traces_list(a.service, a.limit)


async def _traces_get(client: ObsClient, args: BaseModel) -> ToolPayload:
    a = (
        args
        if isinstance(args, TracesGetArgs)
        else TracesGetArgs.model_validate(args.model_dump())
    )
    return await client.traces_get(a.trace_id)


TOOL_SPECS = (
    ToolSpec(
        "logs_search",
        "Search logs using LogsQL query. Filter by severity, service, event, or keywords.",
        LogsSearchArgs,
        _logs_search,
    ),
    ToolSpec(
        "logs_error_count",
        "Count errors by service over a time window. Use to check if there are recent errors.",
        LogsErrorCountArgs,
        _logs_error_count,
    ),
    ToolSpec(
        "traces_list",
        "List recent traces for a service. Returns trace IDs and metadata.",
        TracesListArgs,
        _traces_list,
    ),
    ToolSpec(
        "traces_get",
        "Fetch a specific trace by ID. Shows full span hierarchy and timing.",
        TracesGetArgs,
        _traces_get,
    ),
)
TOOLS_BY_NAME = {spec.name: spec for spec in TOOL_SPECS}
