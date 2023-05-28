import json
import os
import time
from maxid import count_presets


def make_preset(preset, nickname, from_arg):
    path = "presets"
    if not os.path.exists(path):
        os.makedirs(path)

    if from_arg == "":
        from_arg = "anonymous"

    preset_id = count_presets() + 1
    filename = f"{preset_id}.json"


    data = {
        "preset_id": preset_id,
        "content": preset,
        "uploader": from_arg,
        "nickname": nickname,
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        
    }

    filepath = os.path.join(path, filename)

    with open(filepath, "w") as f:
        json.dump(data, f, )
        result = json.dumps(data,)
        print( result )
        return data
        
