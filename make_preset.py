import json
import os
import time


def make_preset(preset, nickname, from_arg):
    def count_presets():
        path = "presets"
        if not os.path.exists(path):
            return 0

        files = os.listdir(path)
        return len(files)

    path = "presets"
    if not os.path.exists(path):
        os.makedirs(path)

    if from_arg == "":
        from_arg = "anonymous"

    preset_id = count_presets() + 1
    filename = f"{preset_id}.json"
    status = "success"

    data = {
        "preset_id": preset_id,
        "content": preset,
        "uploader": from_arg,
        "nickname": nickname,
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        
    }

    filepath = os.path.join(path, filename)

    with open(filepath, "w") as f:
        json.dump(data, f, ensure_ascii=False)
        result = json.dumps(data,ensure_ascii=False)
        print( result )
        return result
        
