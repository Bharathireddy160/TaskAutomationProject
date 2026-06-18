import re


def validate_url(url):
    pattern = re.compile(
        r'^(https?:\/\/)?'
        r'(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})'
        r'(\/.*)?$'
    )

    return re.match(pattern, url)