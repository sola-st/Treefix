# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/clip_ops_test.py
with self.session():
    x = constant_op.constant([-3.0, 0.0, 0.0, 4.0, 0.0, 0.0], shape=[2, 3, 1])
    # Use a nonsensical shape.
    clip = constant_op.constant([1.0, 2.0])
    with self.assertRaises(ValueError):
        _ = clip_ops.clip_by_norm(x, clip)
