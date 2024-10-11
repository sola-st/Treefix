# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
if init_from:
    assert isinstance(init_from, _TypeMap)
    self.types = {
        s: set(other_types) for s, other_types in init_from.types.items()
    }
else:
    self.types = {}
