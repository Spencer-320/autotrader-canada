thonpython
import json
import logging

class Exporter:
    @staticmethod
    def to_json(data, path):
        try:
            with open(path, "w", encoding="utf-8") as fp:
                json.dump(data, fp, indent=2, ensure_ascii=False)
        except Exception as e:
            logging.error(f"Failed to save JSON to {path}: {e}")