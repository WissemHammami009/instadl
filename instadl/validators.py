from urllib.parse import urlparse


def validate_instagram_url(url: str) -> bool:

    try:

        parsed = urlparse(url)

        hostname = parsed.hostname

        if not hostname:
            return False

        hostname = hostname.lower()

        valid_hosts = {
            "instagram.com",
            "www.instagram.com",
        }

        return (
            parsed.scheme in {"http", "https"}
            and hostname in valid_hosts
        )

    except ValueError:
        return False