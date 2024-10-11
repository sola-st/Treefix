# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.AbstractGradientTape(
    use_tape=self.use_tape, persistent=True) as tape:
    tape.watch(self.var)
    val = self.var * self.var
    slice_var = self.var[spec]
    slice_val = val[spec]

    # compute analytic 2nd derivative
    analytic_grad2 = 2 * slice_val

    dy = variables.Variable(
        array_ops.ones_like(slice_var, dtype=dtypes.float32))
    assign = dy.assign(slice_var)

    slice_val_grad = tape.gradient(slice_val, self.var, [dy])
    slice_val_grad2 = tape.gradient(slice_val_grad, dy, [self.var])
self.test.evaluate(assign)
slice_val_grad_evaled, slice_val_grad2_evaled = (
    self.test.evaluate([slice_val_grad, slice_val_grad2]))
analytic_grad2_evaled = self.test.evaluate(analytic_grad2)
self.test.assertAllEqual(slice_val_grad2_evaled, analytic_grad2_evaled)

# compute analytic gradient for slice
np_val_grad = (2 * self.varnp * self.varnp)
np_sliceval_grad = np.zeros(self.var.get_shape())
if isinstance(spec, ops.Tensor):
    spec = self.test.evaluate(spec)
np_sliceval_grad[spec] = np_val_grad[spec]
# verify gradient
self.test.assertAllEqual(slice_val_grad_evaled, np_sliceval_grad)
