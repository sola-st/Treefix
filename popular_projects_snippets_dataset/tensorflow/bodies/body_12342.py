# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/custom_gradient.py
if instance is not None:
    f = self._f.__get__(instance, owner)
    exit(tf_decorator.make_decorator(f, Bind(f, self._d)))
else:
    exit(self)
