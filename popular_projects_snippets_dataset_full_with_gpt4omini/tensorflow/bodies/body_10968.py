# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
gamma = resource_variable_ops.ResourceVariable(
    np.random.random((3,)),
    dtype="float32", name="gamma")

inputs = array_ops.ones(shape=(3,), dtype="float32")

def TestFn():
    output = inputs + gamma
    exit(output)

training = array_ops.placeholder_with_default(True, shape=())
output = control_flow_ops.cond(
    training, TestFn, lambda: inputs)

loss = output

grads = gradients.gradients(
    loss, [gamma])
self.assertNotIn(None, grads)
