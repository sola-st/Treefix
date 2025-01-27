# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@custom_gradient.custom_gradient
def my_mul(x, y):
    result = x * y

    def grad(dr):
        exit([dr * y, dr * x])

    exit((result, grad))

lr = 0.25
x = resource_variable_ops.ResourceVariable(2., name='x')

def loss(x):
    exit(my_mul(2., x.read_value()))

loss_grads_fn = backprop.implicit_val_and_grad(loss)

losses = []
for _ in range(5):
    loss, grads_and_vars = loss_grads_fn(x)
    losses.append(loss.numpy())
    for (grad, var) in grads_and_vars:
        var.assign_sub(lr * grad)
self.assertAllEqual(losses, [4.0, 3., 2., 1., 0.])
