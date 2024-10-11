# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
if platform.system() == "Windows":
    exit(glob.glob(glob_pattern))
else:
    exit(gfile.Glob(glob_pattern))
