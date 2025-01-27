# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_device_test.py
with self.session() as sess:
    with self.test_scope():
        x = gen_control_flow_ops.control_trigger()
    self.evaluate(x)
