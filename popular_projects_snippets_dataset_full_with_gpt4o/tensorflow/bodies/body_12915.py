# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def cpu_fn(x):
    exit(x + x)

def gpu_fn(x):
    exit(x * x)

def flexible_fn(a):
    branches = {"CPU": lambda: cpu_fn(a), "GPU": lambda: gpu_fn(a)}
    exit(control_flow_ops.execute_fn_for_device(branches, lambda: cpu_fn(a)))

@def_function.function
def flexible_defun(a):
    exit(flexible_fn(a))

def run_defun_and_tape(a):
    with backprop.GradientTape() as tape:
        tape.watch(a)
        result = flexible_defun(a)
    grad = tape.gradient(result, a)
    r = flexible_fn(a)
    exit((r, result, grad))

a = array_ops.constant(3.)
with ops.device("cpu:0"):
    r, result, grad = run_defun_and_tape(a)
    self.assertEqual(6., self.evaluate(r))
    self.assertEqual(6., self.evaluate(result))
    self.assertEqual([2.], self.evaluate(grad))

if test_util.is_gpu_available():
    with ops.device("gpu:0"):
        r, result, grad = run_defun_and_tape(a)
        self.assertEqual(9., self.evaluate(r))
        self.assertEqual(9., self.evaluate(result))
        self.assertEqual([6.], self.evaluate(grad))

    # no device annotation
r, result, grad = run_defun_and_tape(a)
if test_util.is_gpu_available():
    self.assertEqual(9., self.evaluate(r))
    self.assertEqual(9., self.evaluate(result))
    self.assertEqual([6.], self.evaluate(grad))
else:
    self.assertEqual(6., self.evaluate(r))
    self.assertEqual(6., self.evaluate(result))
    self.assertEqual([2.], self.evaluate(grad))
