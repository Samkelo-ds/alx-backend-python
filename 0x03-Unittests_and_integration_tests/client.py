#!/usr/bin/env python3
"""Client for fetching GitHub organization data."""

from typing import Dict
import requests


class GithubOrgClient:
    """GitHub client to interact with org data."""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org: str) -> None:
        """Initialize with org name."""
        self.org = org

    def org(self) -> Dict:
        """Get organization data."""
        url = self.ORG_URL.format(org=self.org)
        return requests.get(url).json()
