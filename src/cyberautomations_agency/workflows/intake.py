from __future__ import annotations

from typing import Dict


def build_intake_blueprint(offer_name: str) -> Dict:
    return {
        'offer_name': offer_name,
        'stages': [
            'lead capture',
            'qualification',
            'diagnostic review',
            'proposal draft',
            'human approval',
            'onboarding kickoff',
        ],
        'required_fields': [
            'company_name',
            'website',
            'audience_size',
            'current platforms',
            'pain points',
            'desired outcomes',
            'budget range',
        ],
    }
