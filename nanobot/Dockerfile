ARG REGISTRY_PREFIX_DOCKER_HUB
FROM ${REGISTRY_PREFIX_DOCKER_HUB}astral/uv:python3.14-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
ENV UV_NO_DEV=1
ENV UV_PYTHON_DOWNLOADS=0
ENV UV_PROJECT_ENVIRONMENT=/opt/nanobot-venv

WORKDIR /app

# Copy only what nanobot needs - not the root workspace files.
COPY pyproject.toml README.md /app/nanobot/
COPY --from=workspace mcp /app/mcp
COPY --from=workspace nanobot-websocket-channel /app/nanobot-websocket-channel
COPY . /app/nanobot

# Create a minimal root pyproject.toml for the build.
RUN printf '[project]\nname = "nanobot-build"\nversion = "0.1.0"\nrequires-python = ">=3.14.2"\n\n[tool.uv.workspace]\nmembers = ["nanobot", "mcp/mcp-lms", "nanobot-websocket-channel/nanobot-channel-protocol", "nanobot-websocket-channel/mcp-webchat", "nanobot-websocket-channel/nanobot-webchat"]\n\n[tool.uv.sources]\nmcp-lms = { workspace = true, editable = true }\nmcp-webchat = { workspace = true, editable = true }\nnanobot-channel-protocol = { workspace = true, editable = true }\nnanobot-webchat = { workspace = true, editable = true }\nnanobot-ai = { url = "https://github.com/HKUDS/nanobot/archive/e7d371ec1e6531b28898ec2c869ef338e8dd46ec.zip" }' > /app/pyproject.toml

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --package nanobot

ARG REGISTRY_PREFIX_DOCKER_HUB
FROM ${REGISTRY_PREFIX_DOCKER_HUB}python:3.14.2-slim-bookworm

ARG APP_UID=1000
ARG APP_GID=1000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8

RUN groupadd --gid "${APP_GID}" nonroot \
    && useradd --uid "${APP_UID}" --gid "${APP_GID}" --create-home nonroot

COPY --from=builder --chown=${APP_UID}:${APP_GID} /opt/nanobot-venv /opt/nanobot-venv
COPY --from=builder --chown=${APP_UID}:${APP_GID} /app /app

ENV PATH="/opt/nanobot-venv/bin:$PATH"

USER nonroot
WORKDIR /app/nanobot

CMD ["python", "/app/nanobot/entrypoint.py"]
