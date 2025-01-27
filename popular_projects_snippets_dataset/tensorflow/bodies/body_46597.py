# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
defined_in = anno.getanno(node, anno.Static.DEFINED_VARS_IN)
defined_in_str = set(str(v) for v in defined_in)
if not expected:
    expected = ()
if not isinstance(expected, tuple):
    expected = (expected,)
self.assertSetEqual(defined_in_str, set(expected))
