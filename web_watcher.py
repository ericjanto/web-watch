import difflib
import requests

from bs4 import BeautifulSoup
from os.path import isfile

URL = 'https://www.eca.ed.ac.uk/facility/music-practice-rooms-and-instruments'

# Tag (<tag>) of element to be watched
WATCH_ELEMENT_TAG = 'main'
# ID of element to be watched. Leave empty if not applicable
WATCH_ELEMENT_ID = 'maincontent'

CACHE_FNAME = 'cached_web.txt'

NOTIFICATION_PATH = '/Users/ericjanto/Desktop/WEBSITE_CHANGE.txt'

HEADERS = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}


def main() -> None:
    current = load_current()
    cached = load_cache()
    if update_cache(current, cached):
        diff = ''.join([c[-1]
                       for c in difflib.ndiff(cached, current) if c[0] != '+'])
        notify(diff)


def load_current() -> str:
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    return str(soup.find(WATCH_ELEMENT_TAG, {'id': WATCH_ELEMENT_ID}))


def load_cache() -> str:
    if not isfile(CACHE_FNAME):
        open(CACHE_FNAME, 'x')
        return ''
    with open(CACHE_FNAME, 'r') as f:
        return f.read()


def update_cache(current: str, cached: str) -> bool:
    """
    Updates the cache whilst comparing current and cached.

    Returns:
        True if cache was updated
    """
    if current != cached:
        with open(CACHE_FNAME, 'w') as f:
            f.write(current)
            return True
    return False


def notify(diff):
    if diff and not isfile(NOTIFICATION_PATH):
        open(NOTIFICATION_PATH, 'x')
    with open(NOTIFICATION_PATH, 'w') as f:
        f.write(diff)


if __name__ == '__main__':
    main()
