import json
from pathlib import Path

def load_data(data):
    Path("data/processed").mkdir(parents=True, exist_ok=True)

    with open("data/processed/products.json", "w") as file:
        json.dump(data, file, indent=2)
