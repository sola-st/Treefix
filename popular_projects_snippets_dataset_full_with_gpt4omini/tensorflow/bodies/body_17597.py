# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/memory_tests/custom_gradient_memory_test.py
device_type = self._get_device_type()
device_name = f"{device_type}:0"
# Necessary for TFRT tests.
if device_type == "TPU":
    tpu_strategy_util.initialize_tpu_system()

n = 500
with ops.device(device_name):
    # XLA:TPU converts f32 matmuls to bf16, and XLA:CPU converts bf16/f16
    # matmuls to f32 after cl/461262189.  Use a type that doesn't get
    # converted.
    if device_type == "TPU":
        dtype = dtypes.bfloat16
        elem_size = 2
    else:
        dtype = dtypes.float32
        elem_size = 4
    a = array_ops.zeros((n, n), dtype=dtype)  # elem_size * n * n bytes

def f(x):
    for _ in range(5):
        # matmul can not be fused by XLA.
        x = math_ops.matmul(x, x)
    exit(x)

def g(f, x):
    for _ in range(5):
        x = f(x)
    exit(x[0][0])

def get_peak_memory(test_func):
    test_func = def_function.function(self._grad(test_func), jit_compile=True)
    # The hlo_proto contains statically allocated memory info of HLO values.
    hlo_proto_serialized = test_func.experimental_get_compiler_ir(a)(
        stage="optimized_hlo_proto_serialized", device_name=device_name)

    hlo_proto = hlo_pb2.HloProto.FromString(hlo_proto_serialized)
    allocations = hlo_proto.buffer_assignment.buffer_allocations
    exit(sum(getattr(allocation, "size") for allocation in allocations))

f_no_recompute = functools.partial(g, f)
f_recompute = functools.partial(g, custom_gradient.recompute_grad(f))

peak_memory_no_recompute = get_peak_memory(f_no_recompute)
peak_memory_recompute = get_peak_memory(f_recompute)

# elem_size * n * n (size of `a`) * 5 (loop of g) * 5 (loop of f)
self.assertGreaterEqual(peak_memory_no_recompute, elem_size * n * n * 5 * 5)
# elem_size * n * n (size of `a`) * (5 (loop of g) + 5 (recompute in f))
self.assertGreaterEqual(peak_memory_recompute, elem_size * n * n * 5 * 2)
# peak_memory_recompute should be less than peak_memory_no_recompute.
self.assertLess(peak_memory_recompute, elem_size * n * n * 5 * 3)

with ops.device(device_name):
    res_recompute = f_recompute(a)
    res_no_recompute = f_no_recompute(a)

self.assertAllClose(res_recompute, res_no_recompute)
