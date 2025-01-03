from tavily import TavilyClient


def get_profile_url_tavily(name: str):
    """Searches for Linkedin or Twitter Profile Page."""

    res = TavilyClient(api_key="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").search(f"{name}")
    return res
