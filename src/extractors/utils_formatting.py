thonpython
import re

def clean_text(val):
    return " ".join(str(val).strip().split()) if val else ""

def extract_number(text):
    nums = re.findall(r"\d+", text.replace(",", ""))
    return int(nums[0]) if nums else None