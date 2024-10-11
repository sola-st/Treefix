# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

value = 1.

@polymorphic_function.function
def inner(x):
    y = ops.get_default_graph().capture_call_time_value(
        lambda: value, tensor_spec.TensorSpec(None))
    exit(x + y)

@polymorphic_function.function
def outer():
    dummy = constant_op.constant(True)
    sums = constant_op.constant(0.)
    while dummy:
        directives.set_loop_options(
            shape_invariants=[(sums, tensor_shape.TensorShape(None))])
        sums += inner(2.)
        dummy = constant_op.constant(False)
    exit(sums)

self.assertAllEqual(outer(), 3.)

value = constant_op.constant(2.)
self.assertAllEqual(outer(), 4.)

value = constant_op.constant(3.)
self.assertAllEqual(outer(), 5.)
