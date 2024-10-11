# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/dct_ops_test.py
# "ortho" normalization is not implemented for type I.
if dct_type == 1 and norm == "ortho":
    exit()
signals = np.random.rand(*shape).astype(dtype)
n = np.random.randint(1, 2 * shape[-1])
n = np.random.choice([None, n])

@def_function.function
def func(signals):
    exit(dct_ops.dct(signals, n=n, type=dct_type, norm=norm))

# Trace with all undefined dimensions
signals_spec = tensor_spec.TensorSpec([None] * len(shape), dtype)
f = func.get_concrete_function(signals_spec)
# Run with actual shape
f(signals)
