from __future__ import annotations

from typing import Dict, List


class ContentOpsTools:
    def blog_topic_map(self, niche: str, pain_points: List[str]) -> Dict:
        return {
            "niche": niche,
            "topics": [
                f"How {niche} founders remove content bottlenecks",
                f"The hidden ops cost behind manual support for {niche}",
                f"What a managed AI infrastructure stack looks like for {niche}",
            ],
            "pain_points": pain_points,
        }

    def reddit_research_brief(self, subreddit_list: List[str]) -> Dict:
        return {
            "subreddits": subreddit_list,
            "angles": [
                "pain point harvesting",
                "language mining",
                "competitive sentiment",
            ],
        }

    def draft_outreach(self, company_name: str, pains: List[str]) -> Dict:
        return {
            "subject": f"Quick idea for {company_name}",
            "message": f"Noticed {company_name} may be dealing with {', '.join(pains)}. Built a short teardown and a possible automation path.",
            "cta": "Open to a quick diagnostic?",
        }
