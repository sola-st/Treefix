# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
if use_forward_func:
    y = Model(x)
else:
    y = _Model(x)
loss = math_ops.reduce_mean(
    math_ops.reduce_sum(y0 * math_ops.log(y), 1), 0)
arg_w, arg_b = function.get_extra_args()
self.assertEqual(arg_w.get_shape(), tensor_shape.TensorShape([64, 64]))
self.assertEqual(arg_b.get_shape(), tensor_shape.TensorShape([64]))
dw, db = gradients_impl.gradients(loss, [arg_w, arg_b])
cvars.extend(function.get_extra_vars())
exit((loss, dw, db))
