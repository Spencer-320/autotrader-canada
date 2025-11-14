thonpython
import json
import logging
from pathlib import Path
from extractors.search_page_parser import SearchPageParser
from extractors.listing_parser import ListingParser
from outputs.exporters import Exporter

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def load_input_urls(path: str):
    with open(path, "r", encoding="utf-8") as fp:
        return json.load(fp)

def scrape(urls):
    search_parser = SearchPageParser()
    listing_parser = ListingParser()

    all_listings = []

    for url in urls:
        logging.info(f"Processing search URL: {url}")
        listing_urls = search_parser.get_all_listing_urls(url)

        for listing_url in listing_urls:
            logging.info(f"Fetching listing: {listing_url}")
            data = listing_parser.parse_listing(listing_url)
            if data:
                all_listings.append(data)

    return all_listings

def main():
    input_file = Path(__file__).resolve().parents[1] / "data" / "sample-inputs.json"
    output_file = Path(__file__).resolve().parents[1] / "data" / "sample-output.json"

    urls = load_input_urls(str(input_file))
    results = scrape(urls)

    Exporter.to_json(results, str(output_file))

    logging.info(f"Scraping complete. Saved {len(results)} results to {output_file}")

if __name__ == "__main__":
    main()