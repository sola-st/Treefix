# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
concrete_function_names = sorted(self._proto.concrete_functions.keys())
for name in concrete_function_names:
    if name in self._restored_concrete_functions:
        continue
    self._setup_function_captures(name, self._nodes)
