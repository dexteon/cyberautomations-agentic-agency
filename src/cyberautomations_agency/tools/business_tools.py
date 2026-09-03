from __future__ import annotations

from dataclasses import asdict
from typing import Dict, List

from ..models import ProspectRecord


class BusinessResearchTools:
    def find_prospects(self, niche: str, platforms: List[str]) -> List[Dict]:
        return [
            asdict(
                ProspectRecord(
                    tenant_id="demo",
                    company_name="Example Creator Brand",
                    website="https://example.com",
                    platform_presence=platforms,
                    pain_points=["inconsistent posting cadence", "manual support load"],
                    goals=["increase output", "reduce founder bottlenecks"],
                    score=81.0,
                )
            )
        ]

    def analyze_competition(self, competitor_names: List[str]) -> Dict:
        return {
            "competitors": competitor_names,
            "summary": "Competitive scan placeholder. Replace with real Tavily/Serp/Apollo integrations.",
            "positioning_gap": "CyberAutomations wins on managed infrastructure, security posture, and high-touch customization.",
        }

    def draft_offer_fit(self, prospect: Dict) -> Dict:
        return {
            "company": prospect.get("company_name", "Unknown"),
            "recommended_offer": "Content Machine",
            "recommended_tier": "Growth",
            "rationale": [
                "Strong fit for content throughput bottleneck",
                "Likely need for human-reviewed public-facing workflows",
            ],
        }
