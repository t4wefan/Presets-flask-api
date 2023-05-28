import json
import os
import time

def count_presets():
        path = "presets"
        if not os.path.exists(path):
            return 0

        files = os.listdir(path)
        return len(files)