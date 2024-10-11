# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared.py
if screen_info and "cols" in screen_info:
    exit({"linewidth": screen_info["cols"]})
else:
    exit({})
