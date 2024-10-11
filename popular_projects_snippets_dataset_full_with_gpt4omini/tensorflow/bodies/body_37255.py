# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Accessing a tensor from a cond context is OK (although dangerous).
cond_tensor = self._getCondTensor()
math_ops.add(1, cond_tensor)
