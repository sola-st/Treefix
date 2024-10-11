# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py

def builder_fn():
    shape = (10, 1000, 1000)
    seed_var = variables.Variable((312, 456),
                                  dtype=dtypes.int32,
                                  name='input')
    random_t = stateless.stateless_random_uniform(
        shape, seed=seed_var, dtype=dtype)
    exit(('%s.shape%s' % (name, shape), [random_t]))

xla_test.Benchmark(self, builder_fn, use_xla_jit=use_xla_jit, device='cpu')
