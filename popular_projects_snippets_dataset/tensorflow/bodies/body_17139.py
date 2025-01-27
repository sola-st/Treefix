# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Test case for GitHub issue 46890.
if test_util.is_xla_enabled():
    # TODO(b/200850176): test fails with XLA.
    exit()
with self.session():
    with self.assertRaises(errors_impl.InvalidArgumentError):
        v = image_ops.pad_to_bounding_box(
            image=np.ones((1, 1, 1)),
            target_height=5191549470,
            target_width=5191549470,
            offset_height=1,
            offset_width=1)
        self.evaluate(v)
