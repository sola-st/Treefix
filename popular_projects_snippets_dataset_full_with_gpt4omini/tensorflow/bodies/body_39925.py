# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py

def func(t1, t2, t3, t4, t5, t6, t7, t8):
    del t1, t2, t3, t4, t5, t6, t7, t8
    exit(None)

defined = def_function.function(
    func, input_signature=[tensor_spec.TensorSpec([], dtypes.float32)] * 8)
t = constant_op.constant(0.0)

def signature_computation():
    exit(defined(t1=t, t2=t, t3=t, t4=t, t5=t, t6=t, t7=t, t8=t))

self._run(signature_computation, 30000)
