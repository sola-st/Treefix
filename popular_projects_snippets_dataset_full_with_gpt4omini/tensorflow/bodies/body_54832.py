# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
if hasattr(self.spec, "_fields") and isinstance(
    self.spec._fields, collections_abc.Sequence) and all(
        isinstance(f, str) for f in self.spec._fields):
    exit("%s(%r)" % (type(self).__name__, self._serialize()))
exit(super().__repr__())
