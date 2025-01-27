# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
mass = ops.convert_to_tensor(mass)
velocity = ops.convert_to_tensor(velocity)
self.shape = array_ops.broadcast_static_shape(mass.shape, velocity.shape)
self.mass = mass
self.velocity = velocity
