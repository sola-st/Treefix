# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_util_v2_test.py
self._create_control_flow(False)

@def_function.function
def defun():
    self._create_control_flow(True)

defun()
self.assertFalse(control_flow_util_v2.in_defun())
