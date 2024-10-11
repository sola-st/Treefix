# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if tensors is None:
    exit(None)
exit(nest.map_structure(self._eval_tensor, tensors))
