from __future__ import annotations

import argparse
import json
from .crew import CyberAutomationsAgency
from .logging_config import configure_logging
from .settings import settings


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    configure_logging(settings.log_level)
    agency = CyberAutomationsAgency()

    tenant_profile = {
        'tenant_id': settings.default_tenant,
        'company_name': 'Example Co',
        'website': 'https://cyberautomations.com',
        'niche': 'creator education',
    }

    result = agency.run_business_cycle(
        tenant_profile=tenant_profile,
        business_goal='Find prospects, analyze pains, build outreach, and draft authority content.'
    )

    if args.dry_run:
        print(json.dumps(result, indent=2))
    else:
        print(json.dumps({'status': 'ok', 'tenant': tenant_profile['tenant_id'], 'next_actions': result['next_actions']}, indent=2))


if __name__ == '__main__':
    main()
