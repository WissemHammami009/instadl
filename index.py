import sys

from instadl.downloader import download_instagram_reel
from instadl.validators import validate_instagram_url


def main():

    if len(sys.argv) > 1:
        reel_url = sys.argv[1]
    else:
        reel_url = input(
            "Paste public Instagram Reel URL: "
        ).strip()

    if not reel_url:
        print("No URL provided.")
        sys.exit(1)

    if not validate_instagram_url(reel_url):
        print("Invalid Instagram URL.")
        sys.exit(1)

    download_instagram_reel(reel_url)


if __name__ == "__main__":
    main()