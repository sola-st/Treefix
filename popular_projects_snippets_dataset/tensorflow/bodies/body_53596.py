# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""A context manager for manipulating a default stack."""
self.stack.append(default)
try:
    exit(default)
finally:
    # stack may be empty if reset() was called
    if self.stack:
        if self._enforce_nesting:
            if self.stack[-1] is not default:
                raise AssertionError(
                    "Nesting violated for default stack of %s objects" %
                    type(default))
            self.stack.pop()
        else:
            self.stack.remove(default)
