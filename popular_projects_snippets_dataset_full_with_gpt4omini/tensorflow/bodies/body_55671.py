# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
obj = self._obj
if obj is not None:
    self._obj = None
    self.deleter(obj)
