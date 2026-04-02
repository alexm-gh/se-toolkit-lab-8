---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

# LMS Skill

Use LMS MCP tools to fetch live course data from the backend. Keep responses concise.

## Available Tools

| Tool | When to Use | Parameters |
|------|-------------|------------|
| `lms_health` | User asks if backend is healthy/working | None |
| `lms_labs` | User asks about labs, or you need lab list for selection | None |
| `lms_learners` | User asks about registered learners | None |
| `lms_pass_rates` | User asks about scores, pass rates, attempts | `lab` (required) |
| `lms_timeline` | User asks about submission dates or activity over time | `lab` (required) |
| `lms_groups` | User asks about group performance | `lab` (required) |
| `lms_top_learners` | User asks for top students/leaders | `lab` (required), `limit` (optional, default 5) |
| `lms_completion_rate` | User asks about completion rate | `lab` (required) |
| `lms_sync_pipeline` | User explicitly requests data sync | None |

## Strategy

### When lab is not specified

If the user asks for scores, pass rates, completion, groups, timeline, or top learners **without naming a lab**:

1. Call `lms_labs` first to get available labs
2. **Do NOT pick a lab yourself** — always ask the user to choose
3. If multiple labs exist, use the `structured-ui` skill to present a choice:
   - `type: "choice"` with each lab's `title` as label and `id` as value
   - Pass the current `chat_id` so the choice routes to the active client
4. If only one lab exists, proceed with that lab directly

### Formatting results

- **Percentages**: Format as `85%` not `0.85`
- **Counts**: Use plain numbers like `23 students` not `23.0`
- **Scores**: Round to 1-2 decimal places
- Keep responses brief — state the key metric, not every field

### What can you do?

When asked "what can you do?" or about capabilities:

> I can fetch live data from the LMS backend:
> - List labs and learners
> - Get pass rates, completion rates, and group performance for a lab
> - Show submission timelines and top learners
> - Check backend health
>
> Ask me things like "What labs are available?", "Show me scores for lab-01", or "Which lab has the lowest pass rate?"

## Examples

**User:** "Show me the scores"  
**You:** (Call `lms_labs`, then present choice if multiple labs)

**User:** "lab-02" (after choice)  
**You:** (Call `lms_pass_rates` with `lab="lab-02"`, return concise summary)

**User:** "Is the backend healthy?"  
**You:** (Call `lms_health`, report status and item count)

**User:** "Top 3 students in lab-01"  
**You:** (Call `lms_top_learners` with `lab="lab-01"`, `limit=3`)
