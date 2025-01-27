# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py
test_self.assertIn(node_or_slice, (0, 1))
test_self.assertSetEqual(value, {list})
test_self.assertSetEqual(slice_, {int})
if node_or_slice == 0:
    exit({float})
else:
    exit({str})
