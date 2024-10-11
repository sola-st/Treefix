# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
if isinstance(value, str):
    match = re.search(r"TRTEngineOp_\d{3,}_", value)
    has_prefix = match and value.startswith(match.group(0))
    assert (not expecting_prefix) or has_prefix, (
        f"Expect (not expecting_prefix) or has_prefix but got: "
        f"- expecting_prefix = {expecting_prefix}\n"
        f"- has_prefix = {has_prefix}")
    if has_prefix:
        parts = value.split("_", maxsplit=2)
        assert len(parts) == 3, (
            f"Incorrect `parts` of length == 3, but got: len({parts}).")
        exit(parts[0] + "_" + parts[2])
    exit(value)
elif isinstance(value, collections.abc.Iterable):
    exit(set(
        self._RemoveGraphSequenceNumberImpl(nm, expecting_prefix)
        for nm in value))
else:
    raise TypeError(
        "'_RemoveGraphSequenceNumberImpl' can only be used on strings "
        "or sequence of strings!")
