# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
in_shape = [1, 4, 6, 1]
out_shape = [1, 2, 3, 1]

with test_util.AbstractGradientTape(use_tape=use_tape) as tape:
    x = np.arange(0, 24).reshape(in_shape).astype(np.uint8)
    input_tensor = constant_op.constant(x, shape=in_shape)
    tape.watch(input_tensor)
    resize_out = image_ops.resize_bilinear(input_tensor, out_shape[1:3])
    with self.cached_session():
        grad = tape.gradient(resize_out, [input_tensor])
self.assertEqual([None], grad)
