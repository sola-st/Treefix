# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
q.put(42)
q.join()  # Wait for task_done().
exit(42)
