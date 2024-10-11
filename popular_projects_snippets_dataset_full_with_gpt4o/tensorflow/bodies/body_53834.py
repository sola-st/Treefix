# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Asserts that a and b are the same proto.

    Uses ProtoEq() first, as it returns correct results
    for floating point attributes, and then use assertProtoEqual()
    in case of failure as it provides good error messages.

    Args:
      a: a proto.
      b: another proto.
      msg: Optional message to report on failure.
    """
if not compare.ProtoEq(a, b):
    compare.assertProtoEqual(self, a, b, normalize_numbers=True, msg=msg)
