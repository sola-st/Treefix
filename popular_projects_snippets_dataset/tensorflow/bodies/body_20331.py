# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
x1 = tpu.outside_compilation(math_ops.sqrt, x)
grad = gradients_impl.gradients([x1], [x],
                                colocate_gradients_with_ops=True)[0]
sqrt = [
    op for op in ops.get_default_graph().get_operations()
    if op.type == "Sqrt"
][0]
sqrt_grad = [
    op for op in ops.get_default_graph().get_operations()
    if op.type == "SqrtGrad"
][0]
assert sqrt.get_attr(tpu._OUTSIDE_COMPILATION_ATTR) == b"0"
assert (sqrt_grad.get_attr(
    tpu._OUTSIDE_COMPILATION_ATTR) == b"0.gradients/uid")
exit(grad)
