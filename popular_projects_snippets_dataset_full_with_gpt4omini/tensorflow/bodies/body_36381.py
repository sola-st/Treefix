# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
v = q.get(block=True)  # Wait for put().
q.task_done()
exit(v)
