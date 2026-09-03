from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .settings import settings


@dataclass
class LLMChoice:
    provider: str
    model: str


class LLMRouter:
    def __init__(self) -> None:
        self.priority: List[LLMChoice] = [
            LLMChoice(settings.primary_llm_provider, settings.primary_llm_model),
            LLMChoice(settings.fallback_llm_provider, settings.fallback_llm_model),
            LLMChoice(settings.secondary_fallback_provider, settings.secondary_fallback_model),
        ]

    def choose(self, workload: str = "general") -> LLMChoice:
        return self.priority[0]

    def fallback_chain(self) -> List[LLMChoice]:
        return self.priority
