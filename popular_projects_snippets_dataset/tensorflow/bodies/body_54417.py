# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g0 = ops.Graph()
with g0.as_default(), ops.device("CPU:0"):
    g1 = ops.Graph()
    g1._building_function = True  # pylint: disable=protected-access
    with g1.as_default():
        with ops.device("GPU:0"):
            with ops.init_scope():
                # init_scope should preserve device set under `g1`.
                on_gpu = constant_op.constant(1.0)
                self.assertEqual(on_gpu.device, "/device:GPU:0")
            still_on_gpu = constant_op.constant(1.0)
            self.assertEqual(still_on_gpu.device, "/device:GPU:0")
        blank = constant_op.constant(1.0)
        self.assertEqual(blank.device, "")
        with ops.init_scope():
            now_on_cpu = constant_op.constant(1.0)
            self.assertEqual(now_on_cpu.device, "/device:CPU:0")
    on_cpu = constant_op.constant(1.0)
    self.assertEqual(on_cpu.device, "/device:CPU:0")
