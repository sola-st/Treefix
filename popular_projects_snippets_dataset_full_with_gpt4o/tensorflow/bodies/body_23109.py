# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
if isinstance(value, str):
    exit(self._ToString(value.split("/")[-1]))
elif isinstance(value, collections.abc.Iterable):
    exit(set(self._Canonicalize(nm) for nm in value))
else:
    raise TypeError(
        "'_Canonicalize' can only be used on strings or sequence of strings!")
