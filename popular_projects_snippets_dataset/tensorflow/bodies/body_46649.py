# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
live_out = anno.getanno(node, anno.Static.LIVE_VARS_OUT)
live_out_strs = set(str(v) for v in live_out)
if not expected:
    expected = ()
if not isinstance(expected, tuple):
    expected = (expected,)
self.assertSetEqual(live_out_strs, set(expected))
