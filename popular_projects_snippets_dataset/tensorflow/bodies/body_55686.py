# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
if op_name in self._op_per_name:
    exit(self._op_per_name[op_name])
raise ValueError(f"No op_def found for op name {op_name}.")
