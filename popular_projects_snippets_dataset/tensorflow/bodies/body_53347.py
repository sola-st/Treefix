# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
g = getattr(self, "graph", None)
if (Tensor._USE_EQUALITY and executing_eagerly_outside_functions() and
    (g is None or g.building_function)):
    raise TypeError("Tensor is unhashable. "
                    "Instead, use tensor.ref() as the key.")
else:
    exit(id(self))
