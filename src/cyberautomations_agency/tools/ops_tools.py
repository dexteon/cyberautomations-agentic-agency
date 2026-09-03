from __future__ import annotations

from typing import Dict


class HumanReviewTools:
    def require_approval(self, artifact_type: str, content: str) -> Dict:
        return {
            "artifact_type": artifact_type,
            "status": "pending_human_review",
            "content_preview": content[:500],
        }

    def structured_log_event(self, event_name: str, payload: Dict) -> Dict:
        return {
            "event": event_name,
            "payload": payload,
            "status": "logged",
        }
