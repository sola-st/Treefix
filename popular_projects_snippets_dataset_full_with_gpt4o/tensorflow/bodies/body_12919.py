# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
if not test_util.is_gpu_available():
    exit()

def cpu_fn(x):
    exit(x + x)

def gpu_fn(x):
    exit(x * x)

@def_function.function(jit_compile=True)
def flexible_defun(a):
    branches = {"CPU": lambda: cpu_fn(a), "GPU": lambda: gpu_fn(a)}
    exit(control_flow_ops.execute_fn_for_device(branches, lambda: cpu_fn(a)))

# Always execute the default branch in xla compilation case.
a = array_ops.constant(3.)
r = flexible_defun(a)
self.assertEqual(6., self.evaluate(r))
