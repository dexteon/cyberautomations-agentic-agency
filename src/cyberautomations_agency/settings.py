from __future__ import annotations

import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    app_env: str = os.getenv("APP_ENV", "development")
    app_name: str = os.getenv("APP_NAME", "cyberautomations-agentic-agency")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    default_tenant: str = os.getenv("DEFAULT_TENANT", "demo")
    human_review_required: bool = os.getenv("HUMAN_REVIEW_REQUIRED", "true").lower() == "true"

    primary_llm_provider: str = os.getenv("PRIMARY_LLM_PROVIDER", "anthropic")
    primary_llm_model: str = os.getenv("PRIMARY_LLM_MODEL", "claude-3-7-sonnet-latest")
    fallback_llm_provider: str = os.getenv("FALLBACK_LLM_PROVIDER", "glm")
    fallback_llm_model: str = os.getenv("FALLBACK_LLM_MODEL", "glm-4.5")
    secondary_fallback_provider: str = os.getenv("SECONDARY_FALLBACK_PROVIDER", "gemini")
    secondary_fallback_model: str = os.getenv("SECONDARY_FALLBACK_MODEL", "gemini-2.5-pro")
    model_routing_strategy: str = os.getenv("MODEL_ROUTING_STRATEGY", "priority")

    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    glm_api_key: str = os.getenv("GLM_API_KEY", "")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    openrouter_api_key: str = os.getenv("OPENROUTER_API_KEY", "")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    tavily_api_key: str = os.getenv("TAVILY_API_KEY", "")
    serp_api_key: str = os.getenv("SERP_API_KEY", "")
    apollo_api_key: str = os.getenv("APOLLO_API_KEY", "")
    telegram_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")

    chroma_host: str = os.getenv("CHROMA_HOST", "chromadb")
    chroma_port: int = int(os.getenv("CHROMA_PORT", "8000"))
    chroma_collection_prefix: str = os.getenv("CHROMA_COLLECTION_PREFIX", "ca_")
    data_dir: str = os.getenv("DATA_DIR", "/app/data")
    output_dir: str = os.getenv("OUTPUT_DIR", "/app/output")

    n8n_base_url: str = os.getenv("N8N_BASE_URL", "http://n8n:5678")
    n8n_api_key: str = os.getenv("N8N_API_KEY", "")
    n8n_webhook_secret: str = os.getenv("N8N_WEBHOOK_SECRET", "")

    cyberautomations_base_url: str = os.getenv("CYBERAUTOMATIONS_BASE_URL", "https://cyberautomations.com")
    intake_webhook_url: str = os.getenv("INTAKE_WEBHOOK_URL", "")
    publish_blog: bool = os.getenv("PUBLISH_BLOG", "false").lower() == "true"
    publish_reddit: bool = os.getenv("PUBLISH_REDDIT", "false").lower() == "true"
    publish_social: bool = os.getenv("PUBLISH_SOCIAL", "false").lower() == "true"


settings = Settings()
