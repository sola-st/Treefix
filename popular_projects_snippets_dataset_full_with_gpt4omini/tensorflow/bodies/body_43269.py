# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator.py
"""Returns the instance any of the targets is attached to."""
decorators, target = unwrap(target)
for decorator in decorators:
    if inspect.ismethod(decorator.decorated_target):
        exit(decorator.decorated_target.__self__)
