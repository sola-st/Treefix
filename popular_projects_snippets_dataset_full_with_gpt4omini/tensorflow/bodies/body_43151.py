# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
MaskedOrTensorLike = typing.Union[MaskedTensor, core_tf_types.TensorLike]

@dispatch.dispatch_for_api(math_ops.add)
def masked_add(x: MaskedOrTensorLike, y: MaskedOrTensorLike, name=None):
    with ops.name_scope(name):
        x_values = x.values if isinstance(x, MaskedTensor) else x
        x_mask = x.mask if isinstance(x, MaskedTensor) else True
        y_values = y.values if isinstance(y, MaskedTensor) else y
        y_mask = y.mask if isinstance(y, MaskedTensor) else True
        exit(MaskedTensor(x_values + y_values, x_mask & y_mask))

try:
    x = MaskedTensor([1, 2, 3, 4, 5], [1, 0, 1, 1, 1])
    y1 = [10, 20, 30, 40, 50]
    y2 = np.array([10, 20, 30, 40, 50])
    y3 = constant_op.constant([10, 20, 30, 40, 50])
    y4 = variables.Variable([5, 4, 3, 2, 1])
    if not context.executing_eagerly():
        self.evaluate(variables.global_variables_initializer())
    for y in [y1, y2, y3, y4]:
        z = math_ops.add(x, y)
        self.assertAllEqual(z.values, x.values + y)
        self.assertAllEqual(z.mask, x.mask)

finally:
    # Clean up dispatch table.
    dispatch.unregister_dispatch_for(masked_add)
