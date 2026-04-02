# Lab 8 — Report

## Task 1A — Bare agent

<!--### Q1: "What is 2+2?"-->


2 + 2 = 4


<!--### Q2: "What is the agentic loop?"-->

The agentic loop is the fundamental cycle that an AI agent follows to accomplish tasks autonomously. It typically consists of these core stages:


**The Agentic Loop Cycle:**

1. **Perceive** — Gather information from the environment
   - Read user input
   - Observe current state (files, system, context)
   - Retrieve relevant memories or knowledge

2. **Reason** — Process and plan
   - Analyze the situation
   - Determine goals and constraints
   - Decide on next actions or create a plan

3. **Act** — Execute decisions
   - Call tools (file operations, web search, commands, etc.)
   - Modify the environment
   - Communicate results

4. **Reflect** — Evaluate outcomes
   - Check if the goal was achieved
   - Learn from errors or unexpected results
   - Adjust strategy if needed

Then the loop repeats until the task is complete.

**Why It Matters:**

This loop enables autonomous behavior — the agent doesn't just respond once, but iteratively works toward a goal, adapting based on feedback from each action. More sophisticated agents may also include:

- Memory updates — Storing learned information
- Multi-step planning — Breaking complex tasks into subtasks
- Self-correction — Detecting and fixing mistakes

In my case, every time you give me a task, I go through this loop: I read the request, decide what tools to use, execute them, and then respond or continue iterating based on the results.


<!--### Q3: "What labs are available in our LMS?"-->

The agent **does not have access to the live LMS backend** yet. It explored the local filesystem using built-in tools (`list_dir`, `read_file`) and found lab task descriptions in the repository:


Based on my exploration of the workspace, here are the available labs in your LMS:

**Required Labs:**
1. Task 1 — Set Up the Agent (install nanobot, configure Qwen API, add MCP tools, write skill prompt)
2. Task 2 — Deploy and Connect a Web Client (Dockerize nanobot, add WebSocket channel + Flutter chat UI)
3. Task 3 — Give the Agent New Eyes (explore observability data, write log/trace MCP tools)
4. Task 4 — Diagnose a Failure and Make the Agent Proactive (investigate a failure, schedule in-chat health checks, fix a planted bug)

**Optional Labs:**
1. Task 1 — Add a Telegram Bot Client (same agent, different interface)

This is Lab 8 — "The Agent is the Interface" from the Software Engineering Toolkit course. The lab focuses on building an AI agent (nanobot) as a      
natural-language interface to an LMS system, with capabilities for querying data, observability tools, and proactive health checks.                    

Would you like me to read the details of any specific task?                                                      


## Task 1B — Agent with LMS tools

<!--### Q1: "What is the agentic loop?"-->


The agentic loop refers to the iterative process that autonomous AI agents follow to accomplish tasks. While the specific implementation can vary between different AI systems, a typical     
agentic loop includes these core phases:                                                                                                                                                      

 1 Perception/Observation: The agent gathers information from its environment, user requests, or available data sources.                                                                      
 2 Reasoning/Planning: The agent analyzes the gathered information, determines what needs to be done, and formulates a plan of action.                                                        
 3 Action: The agent executes specific tools, commands, or operations to move toward its goal.                                                                                                
 4 Observation/Evaluation: The agent observes the results of its actions and evaluates progress toward the goal.                                                                              
 5 Iteration: The agent returns to planning based on new observations, adjusting its approach as needed until the task is completed.                                                          

This cycle continues until the agent achieves its objective or determines that it cannot proceed further. The loop allows AI agents to handle complex, multi-step tasks by breaking them down 
into smaller, manageable actions while adapting to new information or unexpected outcomes during execution.                                                                                   

In my case as nanobot, I follow this pattern by receiving your requests, analyzing them, using appropriate tools to gather information or perform actions, observing the results, and then    
determining the next steps in our conversation.    


<!--### Q2: "Is the LMS backend healthy?">


Let me check the health of the LMS backend:                                                                                                                

Yes, the LMS backend is healthy. The system is operational with 56 items and no errors reported.

<!--### Q3: "What labs are available?"-->

I'll check what labs are available in the LMS system for you.                                                                                          

Here are the available labs in the LMS system:                                                                                                         

 1 Lab 01 – Products, Architecture & Roles                                                                                                             
 2 Lab 02 — Run, Fix, and Deploy a Backend Service                                                                                                     
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy                                                                                             
 4 Lab 04 — Testing, Front-end, and AI Agents                                                                                                          
 5 Lab 05 — Data Pipeline and Analytics Dashboard                                                                                                      
 6 Lab 06 — Build Your Own Agent                                                                                                                       
 7 Lab 07 — Build a Client with an AI Coding Agent                                                                                                     
 8 Lab 08                                                                                                                   

## Task 1C — Skill prompt

<!--### Q1: "Show me the scores"-->


I'll help you check the scores. First, let me see what labs are available in the system.

I can see there are 8 labs available in the system. To show you the scores, I need to know which specific lab you're interested in. Here are the       
available labs:                                                                                                                                        

 1 Lab 01 – Products, Architecture & Roles                                                                                                             
 2 Lab 02 — Run, Fix, and Deploy a Backend Service                                                                                                     
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy                                                                                             
 4 Lab 04 — Testing, Front-end, and AI Agents                                                                                                          
 5 Lab 05 — Data Pipeline and Analytics Dashboard                                                                                                      
 6 Lab 06 — Build Your Own Agent                                                                                                                       
 7 Lab 07 — Build a Client with an AI Coding Agent                                                                                                     
 8 lab-08                                                                                                                                              

Could you please specify which lab you'd like to see the scores for?                                                        


## Task 2A — Deployed agent

nanobot-1  | Using config: /app/nanobot/config.resolved.json
nanobot-1  | 🐈 Starting nanobot gateway version 0.1.4.post5 on port 18790...
nanobot-1  | 2026-04-02 15:12:02.818 | DEBUG    | nanobot.channels.registry:discover_all:64 - Skipping built-in channel 'matrix': Matrix dependencies not installed. Run: pip install nanobot-ai[matrix]
nanobot-1  | Warning: No channels enabled
nanobot-1  | ✓ Heartbeat: every 1800s
nanobot-1  | 2026-04-02 15:12:02.993 | INFO     | nanobot.cron.service:start:202 - Cron service started with 0 jobs
nanobot-1  | 2026-04-02 15:12:02.993 | INFO     | nanobot.heartbeat.service:start:124 - Heartbeat started (every 1800s)
nanobot-1  | 2026-04-02 15:12:03.147 | WARNING  | nanobot.channels.manager:start_all:82 - No channels enabled
nanobot-1  | 2026-04-02 15:12:04,300 INFO [mcp.server.lowlevel.server] [server.py:727] [trace_id=0 span_id=0 resource.service.name=mcp-lms trace_sampled=False] - Processing request of type ListToolsRequest
nanobot-1  | 2026-04-02 15:12:04.304 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_health' from server 'lms'
nanobot-1  | 2026-04-02 15:12:04.304 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_labs' from server 'lms'
nanobot-1  | 2026-04-02 15:12:04.304 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_learners' from server 'lms'
nanobot-1  | 2026-04-02 15:12:04.304 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_pass_rates' from server 'lms'
nanobot-1  | 2026-04-02 15:12:04.304 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_timeline' from server 'lms'
nanobot-1  | 2026-04-02 15:12:04.304 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_groups' from server 'lms'
nanobot-1  | 2026-04-02 15:12:04.304 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_top_learners' from server 'lms'
nanobot-1  | 2026-04-02 15:12:04.304 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_completion_rate' from server 'lms'
nanobot-1  | 2026-04-02 15:12:04.304 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_sync_pipeline' from server 'lms'
nanobot-1  | 2026-04-02 15:12:04.304 | INFO     | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'lms': connected, 9 tools registered
nanobot-1  | 2026-04-02 15:12:04.304 | INFO     | nanobot.agent.loop:run:280 - Agent loop started

## Task 2B — Web client

![Nanobot chat](task2a_1.png)
![Nanobot chat](task2a_2.png)

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
