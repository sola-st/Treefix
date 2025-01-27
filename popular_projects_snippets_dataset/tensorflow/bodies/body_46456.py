# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py
if not isinstance(expected, tuple):
    expected = expected,
self.assertSetEqual(
    set(anno.getanno(node, anno.Static.TYPES)), set(expected))
