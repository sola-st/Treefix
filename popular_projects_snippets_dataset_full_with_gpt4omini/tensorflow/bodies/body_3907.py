# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect.py
source = inspect.getsource(obj)
name = source.split("=")[0].strip()
exit(name)
