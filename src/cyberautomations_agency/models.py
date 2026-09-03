from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class TenantContext:
    tenant_id: str
    company_name: str
    website: str = ""
    niche: str = ""
    notes: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ProspectRecord:
    tenant_id: str
    company_name: str
    contact_name: str = ""
    website: str = ""
    platform_presence: List[str] = field(default_factory=list)
    pain_points: List[str] = field(default_factory=list)
    goals: List[str] = field(default_factory=list)
    score: float = 0.0
