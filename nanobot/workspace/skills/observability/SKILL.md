---
name: observability
description: Use VictoriaLogs and VictoriaTraces MCP tools for observability data
always: true
---

# Observability Skill

Use VictoriaLogs and VictoriaTraces MCP tools to investigate errors and trace request flows. Keep responses concise.

## Available Tools

| Tool | When to Use | Parameters |
|------|-------------|------------|
| `logs_search` | Search for specific log patterns, errors, or trace IDs | `query` (LogsQL), `limit`, `time_range` |
| `logs_error_count` | Quick check if there are recent errors | `service` (optional), `time_range` |
| `traces_list` | List recent traces for a service | `service` (optional), `limit` |
| `traces_get` | Fetch full trace details by ID | `trace_id` (required) |

## Strategy

### When user asks "What went wrong?" or "Check system health"

Do a full one-shot investigation:

1. **`logs_error_count`** with a fresh recent window (e.g., `time_range="10m"`, `service="Learning Management Service"`)
2. If errors exist, **`logs_search`** scoped to the failing service:
   - Query: `severity:ERROR service.name:"Learning Management Service"`
   - Extract `trace_id` from the most recent error log
3. **`traces_get`** for that `trace_id` to see the full failure path
4. **Summarize** with both log evidence AND trace evidence:
   - Name the affected service
   - Name the root failing operation
   - Mention any discrepancy between what the logs show vs what the backend reports
   - Don't dump raw JSON

### When user asks about errors in a time window

1. Start with `logs_error_count` for the LMS backend service with the specified time window
2. If errors exist, use `logs_search` to find recent error logs:
   - Query: `severity:ERROR service.name:"Learning Management Service"`
   - Extract any `trace_id` from the log results
3. If you found a `trace_id`, use `traces_get` to fetch the full trace and understand the failure
4. Summarize findings concisely — don't dump raw JSON

### When user asks about a specific request

1. If they provide a `trace_id`, use `traces_get` directly
2. If not, use `logs_search` to find matching logs, then extract `trace_id`

### Query tips

- VictoriaLogs LogsQL examples:
  - `severity:ERROR service.name:"Learning Management Service" _time:10m`
  - `event:db_query service.name:"Learning Management Service" _time:1h`
  - `trace_id:abc123...`

- VictoriaTraces:
  - Use `traces_list` to find recent traces, then `traces_get` for details
  - Trace response shows span hierarchy with timing

## Response style

- Summarize, don't dump: "Found 3 errors in the last 10 minutes. The most recent was a database connection failure at 14:32. Trace ID: abc123..."
- If no errors: "No errors found for the LMS backend in the last 10 minutes."
- Include trace IDs when relevant so the user can look them up

## Examples

**User:** "Any errors in the last hour?"
**You:** (Call `logs_error_count` with `time_range="1h"`, `service="Learning Management Service"`)

**User:** "What went wrong with the last request?"
**You:** (Call `logs_search` with recent time range, extract `trace_id`, then `traces_get`)

**User:** "Show me the trace for request abc123"
**You:** (Call `traces_get` with `trace_id="abc123"`)
