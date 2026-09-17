def progress_hook(data):

    status = data.get("status")

    if status == "downloading":

        percent = data.get(
            "_percent_str",
            ""
        ).strip()

        speed = data.get(
            "_speed_str",
            ""
        ).strip()

        eta = data.get(
            "_eta_str",
            ""
        ).strip()

        print(
            f"\rDownloading: {percent} | "
            f"Speed: {speed} | "
            f"ETA: {eta}",
            end="",
            flush=True
        )

    elif status == "finished":

        print()
        print("Download finished. Processing video...")