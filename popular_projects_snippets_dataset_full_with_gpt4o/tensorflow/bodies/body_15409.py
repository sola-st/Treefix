# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
# For some tests, the inputs/outputs to the function need to be
# constructed late, because they contain tensors.
if callable(kwargs):
    kwargs = kwargs()
if callable(args):
    args = args()
if callable(expected):
    expected = expected()

kwargs = kwargs or {}
if rtol is not None:
    assert_fn = lambda x, y: self.assertAllClose(x, y, rtol=rtol)
else:
    assert_fn = self.assertAllEqual

result = op(*args, **kwargs)
if isinstance(expected, DynamicRaggedShape):
    self.assertDynamicRaggedShapeEqual(expected, result)
elif result_is_list:
    self.assertLen(result, len(expected))
    for (r, e) in zip(result, expected):
        assert_fn(r, e)
else:
    assert_fn(result, expected)
