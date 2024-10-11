# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/memory_tests/custom_gradient_memory_test.py
device_type = self._get_device_type()
device_name = f"{device_type}:0"

if device_type == "TPU":
    self.skipTest("XLA is required for TPU.")

if device_type == "CPU":
    self.skipTest("b/185371422: get_memory_info does't support CPU yet.")

config.reset_memory_stats(device_name)
base_memory = config.get_memory_info(device_name)["current"]
n = 500
with ops.device(device_name):
    a = array_ops.ones((n, n), dtype=dtypes.float16)

def f(x):
    for _ in range(5):
        x = math_ops.matmul(x, x)
    exit(x)

def g(f, x):
    for _ in range(5):
        x = f(x)
    exit(x[0][0])

def run(test_func):
    with ops.device(device_name):
        if mode == "eager":
            exit(self._grad(test_func)(a))
        else:
            exit(def_function.function(self._grad(test_func))(a))

f_no_recompute = functools.partial(g, f)
f_recompute = functools.partial(g, custom_gradient.recompute_grad(f))

# The result is not saved so the base memory will stay the same.
run(f_no_recompute)
peak_memory_no_recompute = (
    config.get_memory_info(device_name)["peak"] - base_memory)

config.reset_memory_stats(device_name)
run(f_recompute)
peak_memory_recompute = (
    config.get_memory_info(device_name)["peak"] - base_memory)

# 2 * n * n (size of `a`) * 5 (loop of f) * 5 (loop of g)
self.assertGreaterEqual(peak_memory_no_recompute, 2 * n * n * 5 * 5)
# 2 * n * n (size of `a`) * (5 (loop of g) + 5 (recompute in f))
self.assertGreaterEqual(peak_memory_recompute, 2 * n * n * 5 * 2)
# peak_memory_recompute should be less than peak_memory_no_recompute.
self.assertLess(peak_memory_recompute, 2 * n * n * 5 * 3)

res_no_recompute = run(f_no_recompute)
res_recompute = run(f_recompute)
self.assertAllClose(res_no_recompute, res_recompute)
