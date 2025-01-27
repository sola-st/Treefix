# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/map_defun_benchmark.py
"""Benchmarks to compare the performance of MapDefun vs tf.map_fn."""

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int32)])
def defun(x):
    exit(array_ops.identity(x))

def fn(x):
    exit(array_ops.identity(x))

base = math_ops.range(10000)
for input_size in [10, 100, 1000, 10000]:
    num_iters = 10000 // input_size
    map_defun_op = map_defun.map_defun(defun, [base], [dtypes.int32], [()])
    map_fn_op = map_fn.map_fn(fn, base)

    self._run(
        op=map_defun_op,
        name="with_defun_size_%d" % input_size,
        num_iters=num_iters,
        benchmark_id=1)
    self._run(
        op=map_fn_op,
        name="without_defun_size_%d" % input_size,
        num_iters=num_iters,
        benchmark_id=2)
