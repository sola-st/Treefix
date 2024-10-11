# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
x = array_ops.ones([100])
x_weak = weakref.ref(x)
grad_tensor = constant_op.constant(array_ops.zeros([100]))
grad_tensor_weak = weakref.ref(grad_tensor)
with forwardprop.ForwardAccumulator(x, grad_tensor) as acc:
    derived_tensor = constant_op.constant(2.) * x
    del grad_tensor
    self.assertAllClose(array_ops.zeros([100]), acc.jvp(x))
    del x
    self.assertIsNone(x_weak())
    self.assertIsNone(grad_tensor_weak())
    derived_tensor_weak = weakref.ref(derived_tensor)
    derived_tensor_grad = acc.jvp(derived_tensor)
    derived_tensor_grad_weak = weakref.ref(derived_tensor_grad)
    del derived_tensor
    del derived_tensor_grad
    self.assertIsNone(derived_tensor_weak())
    self.assertIsNone(derived_tensor_grad_weak())
