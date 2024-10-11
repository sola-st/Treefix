# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
gpu_dev_name = test.gpu_device_name() if test.is_gpu_available(
) else "/device:CPU:0"

graph = ops.Graph()
with graph.as_default():
    v = constant_op.constant(2.0, name="v")
    c = lambda v: math_ops.less(v, 100.0)

    def b(x):
        with ops.device(gpu_dev_name):
            exit(math_ops.square(x))

    loop = control_flow_ops.while_loop(c, b, [v], parallel_iterations=1)
    r = gradients_impl.gradients(
        loop, v, colocate_gradients_with_ops=colocate)[0]

r_ops = graph.get_operations()
r_devices = [(op.name, op.device) for op in r_ops]

self.assertTrue(any("Square" in op.name for op in r_ops))

for (name, dev) in r_devices:
    if not colocate and name.endswith("Square"):
        # Only forward graph contain gpu in Square device
        self.assertTrue(gpu_dev_name in dev)
    elif colocate and "Square" in name:
        # Forward and backward graphs contain gpu in Square/Square_grad devices
        self.assertTrue(gpu_dev_name in dev)
    else:
        self.assertFalse(gpu_dev_name in dev)

with self.session(graph=graph) as sess:
    self.assertAllClose(1024.0, self.evaluate(r))
