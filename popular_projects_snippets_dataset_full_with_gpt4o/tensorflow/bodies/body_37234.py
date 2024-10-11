# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
if not context.executing_eagerly():
    exit()
input_data = [1, 2, 3, 4]
vf, vt = control_flow_ops.switch(input_data, False)
self.assertAllEqual(vf, input_data)
self.assertAllEqual(vt, [])
