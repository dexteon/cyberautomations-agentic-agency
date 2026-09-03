# CyberAutomations Agentic Agency

Production-oriented CrewAI scaffold for running CyberAutomations as an internal agentic business operating system.

## What this repo does

This scaffold is designed to help CyberAutomations operate as a security-first, multi-tenant-ready managed AI infrastructure agency. It includes:

- Leadership and orchestration crews for business operations.
- Prospecting, research, outreach, content, competitive intelligence, intake, solution design, and proposal workflows.
- Human-in-the-loop approval gates for all public-facing content.
- Local-first development with Docker Compose, `.env`, structured logs, and ChromaDB.
- Provider routing with Claude Max primary, GLM fallback, then Gemini or other configured providers.

## Suggested first use cases

1. Find and score prospects in your ICP.
2. Research pain points, goals, platforms, and market signals.
3. Draft outreach, diagnostics, teardown notes, and proposal material.
4. Run content/blog/Reddit/social research and draft queues.
5. Support client-facing intake and onboarding automation.

## Repo layout

- `src/cyberautomations_agency/config/agents.yaml` - agent definitions
- `src/cyberautomations_agency/config/tasks.yaml` - task definitions
- `src/cyberautomations_agency/main.py` - entrypoint
- `src/cyberautomations_agency/crew.py` - crew and workflow orchestration
- `src/cyberautomations_agency/llm_router.py` - provider/model routing
- `src/cyberautomations_agency/logging_config.py` - structured logging
- `src/cyberautomations_agency/tools/` - tool implementations and stubs
- `docker-compose.yml` - local stack
- `Makefile` - common commands
- `.env.example` - environment template

## Notes

- Start local with Docker and `.env`, then migrate pieces to cyberautomations.com.
- Publishing destinations are intentionally configurable because your final channel mix is not locked yet.
- This scaffold plans for multi-tenancy from the start with tenant-aware data paths, metadata, and config shape.
