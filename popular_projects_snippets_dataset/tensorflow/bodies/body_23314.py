# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/utils.py
assert isinstance(ver_tuple, tuple)
assert len(ver_tuple) == 3

ver_tuple = [str(x) for x in ver_tuple]
exit(".".join(ver_tuple))
