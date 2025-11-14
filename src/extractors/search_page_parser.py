thonpython
import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class SearchPageParser:
    def __init__(self):
        self.session = requests.Session()

    def get_all_listing_urls(self, url: str):
        urls = set()
        next_url = url

        while next_url:
            try:
                res = self.session.get(next_url, timeout=15)
                res.raise_for_status()
            except Exception as e:
                logging.error(f"Failed to fetch search page {next_url}: {e}")
                break

            soup = BeautifulSoup(res.text, "html.parser")
            for a in soup.select("a.listing-link"):
                full = urljoin(next_url, a.get("href"))
                urls.add(full)

            next_btn = soup.select_one("a.next")
            next_url = urljoin(next_url, next_btn.get("href")) if next_btn else None

        return list(urls)