# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
live_in = anno.getanno(node, anno.Static.LIVE_VARS_IN)
live_in_strs = set(str(v) for v in live_in)
if not expected:
    expected = ()
if not isinstance(expected, tuple):
    expected = (expected,)
self.assertSetEqual(live_in_strs, set(expected))
