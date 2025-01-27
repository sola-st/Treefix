# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_util.py
if indices is None:
    indices = ()
if tangents is None:
    tangents = []
exit(super(TangentInfo, cls).__new__(cls, indices, tangents))
