# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
v = resource_variable_ops.ResourceVariable([0.0, 1.0, 2.0])

def sum_gather():
    exit(math_ops.reduce_sum(array_ops.gather(v, [1, 2])))

grad_fn = backprop.implicit_grad(sum_gather)
gradient = grad_fn()
defun_grad_fn = backprop.implicit_grad(
    polymorphic_function.function(sum_gather))
defun_gradient = defun_grad_fn()
self.assertEqual(len(gradient), len(defun_gradient))

gradient = gradient[0][0]
defun_gradient = defun_gradient[0][0]
self.assertAllEqual(gradient.values, defun_gradient.values)
self.assertAllEqual(gradient.indices, defun_gradient.indices)
self.assertAllEqual(gradient.dense_shape, defun_gradient.dense_shape)
