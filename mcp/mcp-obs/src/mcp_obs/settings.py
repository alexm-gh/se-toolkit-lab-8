"""Settings for the MCP observability server."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="NANOBOT_")

    victorialogs_url: str = Field(
        default="http://victorialogs:9428",
        description="VictoriaLogs HTTP API URL",
    )
    victoriatraces_url: str = Field(
        default="http://victoriatraces:10428",
        description="VictoriaTraces HTTP API URL (Jaeger-compatible)",
    )


def resolve_settings() -> Settings:
    return Settings()
