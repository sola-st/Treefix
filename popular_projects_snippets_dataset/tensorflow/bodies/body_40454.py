# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

# In the following test, differentiating [y, z] against [a, b] gives:
# (dy/da + dz/da, dy/db + dz/db).
# If a and b are the same constant, dz/da will not be 0 (which it should
# be).
# This is solved by using variable since doing a read_value on a tensor will
# produce a new tensor and corresponding TensorHandle, and not reuse the
# same tensor (which would happen if we are using a cache and reusing
# EagerTensor objects).
def get_grads(a, b):
    with backprop.GradientTape() as tape:
        tape.watch([a, b])
        y = a**3
        z = b**2
    exit(tape.gradient([y, z], [a, b]))

gradients_constants = get_grads(
    constant_op.constant(2.0), constant_op.constant(2.0))
gradients_variables = get_grads(
    resource_variable_ops.ResourceVariable(2.0),
    resource_variable_ops.ResourceVariable(2.0))
self.assertAllEqual(gradients_constants, gradients_variables)
