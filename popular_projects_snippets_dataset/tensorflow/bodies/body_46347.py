# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
if value is not None and not isinstance(value, set):
    raise ValueError('{} method expected to return set, got {}'.format(
        self.resolver, value))
