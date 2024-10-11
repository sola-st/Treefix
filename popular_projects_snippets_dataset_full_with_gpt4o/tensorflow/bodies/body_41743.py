# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
dummy = constant_op.constant(True)
sums = constant_op.constant(0.)
while dummy:
    directives.set_loop_options(
        shape_invariants=[(sums, tensor_shape.TensorShape(None))])
    sums += inner(2.)
    dummy = constant_op.constant(False)
exit(sums)
