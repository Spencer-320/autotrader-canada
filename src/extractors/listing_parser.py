thonpython
import logging
import requests
from bs4 import BeautifulSoup
from .utils_formatting import clean_text, extract_number

class ListingParser:
    def __init__(self):
        self.session = requests.Session()

    def parse_listing(self, url: str):
        try:
            res = self.session.get(url, timeout=15)
            res.raise_for_status()
        except Exception as e:
            logging.error(f"Failed to fetch listing {url}: {e}")
            return None

        soup = BeautifulSoup(res.text, "html.parser")

        data = {
            "url": url,
            "make": clean_text(soup.select_one(".atcui-make") or ""),
            "model": clean_text(soup.select_one(".atcui-model") or ""),
            "year": extract_number(clean_text(soup.select_one(".atcui-year") or "")),
            "price_str": clean_text(soup.select_one(".price") or ""),
            "price_cad": extract_number(clean_text(soup.select_one(".price") or "")),
            "mileage_str": clean_text(soup.select_one(".mileage") or ""),
            "mileage_km": extract_number(clean_text(soup.select_one(".mileage") or "")),
            "body_type": clean_text(soup.select_one(".bodyType") or ""),
            "fuel_type": clean_text(soup.select_one(".fuelType") or ""),
            "drivetrain": clean_text(soup.select_one(".drivetrain") or ""),
            "transmission": clean_text(soup.select_one(".transmission") or ""),
            "city": clean_text(soup.select_one(".city") or ""),
            "province": clean_text(soup.select_one(".province") or ""),
            "seller_name": clean_text(soup.select_one(".seller-name") or ""),
            "description": clean_text(soup.select_one(".description") or ""),
        }

        imgs = [img["src"] for img in soup.select("img") if img.get("src")]
        data["image_urls"] = imgs

        return data