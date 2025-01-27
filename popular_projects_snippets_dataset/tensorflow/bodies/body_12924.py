# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def default_fn(x):
    exit(x)

def tpu_fn(x):
    exit(x * x * x)

def flexible_fn(a):
    branches = {"TPU": lambda: tpu_fn(a)}
    exit(control_flow_ops.execute_fn_for_device(
        branches, default_fn=lambda: default_fn(a)))

@def_function.function
def flexible_defun(a):
    exit(flexible_fn(a))

a = array_ops.constant(3.)
with ops.device("cpu:0"):
    result_defun = flexible_defun(a)
    result_defun = flexible_fn(a)
    self.assertEqual(3., self.evaluate(result_defun))
    # execute_fn_for_device is not inside defun_function.
    result = flexible_fn(a)
    self.assertEqual(3., self.evaluate(result))

if test_util.is_gpu_available():
    with ops.device("gpu:0"):
        result_defun = flexible_defun(a)
        self.assertEqual(3., self.evaluate(result_defun))
        # execute_fn_for_device is not inside defun_function.
        result = flexible_fn(a)
        self.assertEqual(3., self.evaluate(result))
