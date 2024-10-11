# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
y1 = np.zeros((2, 2), dtype=np.float32)
y2 = array_ops.gather(x1, [2]) * x2
y3 = array_ops.gather(x1, [2])
exit((y1, y2, y3))
