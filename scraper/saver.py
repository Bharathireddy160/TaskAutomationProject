import os


def save_title(title):

    os.makedirs(
        "output",
        exist_ok=True
    )

    file_path = "output/website_title.txt"

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(title)