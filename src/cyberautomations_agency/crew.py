from __future__ import annotations

from pathlib import Path
from typing import Any, Dict
import yaml
import structlog

from .llm_router import LLMRouter
from .settings import settings
from .tools import BusinessResearchTools, ContentOpsTools, HumanReviewTools

logger = structlog.get_logger()


class CyberAutomationsAgency:
    def __init__(self) -> None:
        self.router = LLMRouter()
        self.business_tools = BusinessResearchTools()
        self.content_tools = ContentOpsTools()
        self.ops_tools = HumanReviewTools()
        self.agents = self._load_yaml('config/agents.yaml')
        self.tasks = self._load_yaml('config/tasks.yaml')

    def _load_yaml(self, relative_path: str) -> Dict[str, Any]:
        here = Path(__file__).resolve().parent
        path = here / relative_path
        with path.open('r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def run_business_cycle(self, tenant_profile: Dict[str, Any], business_goal: str) -> Dict[str, Any]:
        llm = self.router.choose('leadership')
        logger.info('business_cycle_started', tenant=tenant_profile.get('tenant_id', settings.default_tenant), llm_provider=llm.provider, llm_model=llm.model)

        prospect_sample = self.business_tools.find_prospects(
            niche=tenant_profile.get('niche', 'creator education'),
            platforms=['YouTube', 'Instagram', 'Skool', 'Email']
        )
        competition = self.business_tools.analyze_competition(['Repurpose.io', 'OpusClip', 'Coachvox AI'])
        topic_map = self.content_tools.blog_topic_map(tenant_profile.get('niche', 'creator education'), ['content bottleneck', 'support fatigue'])

        result = {
            'tenant': tenant_profile,
            'goal': business_goal,
            'llm': {'provider': llm.provider, 'model': llm.model},
            'priority_lane': 'growth-and-content',
            'prospect_sample': prospect_sample,
            'competition_snapshot': competition,
            'content_topics': topic_map,
            'next_actions': [
                'Review prospect sample and define top 25 targets',
                'Approve one outreach angle and one teardown format',
                'Approve first 3 blog topics for drafting',
                'Design intake automation flow in n8n',
            ],
        }
        logger.info('business_cycle_completed', tenant=tenant_profile.get('tenant_id', settings.default_tenant), next_actions=len(result['next_actions']))
        return result
