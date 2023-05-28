import os
import json
from maxid import count_presets

def read_preset(id):
    filename = f"presets/{id}.json"
    status = "ok" if os.path.isfile(filename) else "error"
    preset_data = {}
    if status == "ok":
        with open(filename, "r") as f:
            preset_data = json.load(f)
    preset_data["status"] = status
    preset_data["max_id"] = count_presets()

    return preset_data