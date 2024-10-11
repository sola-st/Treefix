# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with ops.Graph().as_default() as g:
    with self.session(
        graph=g, config=config_pb2.ConfigProto(device_count={"CPU": 2})):

        def fn2():
            with ops.device("/device:CPU:1"):
                c = constant_op.constant(3.0)
                self.assertEqual("/device:CPU:1", c.op.device)
                exit(c)

        with ops.device("/device:CPU:0"):
            self.assertEqual(
                cond_v2.cond_v2(constant_op.constant(True), fn2, fn2).eval(), 3)

            d = constant_op.constant(4.0)
            self.assertEqual("/device:CPU:0", d.op.device)
