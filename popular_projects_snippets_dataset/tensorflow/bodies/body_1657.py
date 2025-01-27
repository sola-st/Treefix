# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
"""Tests whole-function forced-compilation.

    This test checks that stateless_random_* can be used in forced-compilation
    scenarios (e.g. TPU). The new version of stateless_random_* requires the
    intermediate tensor `alg` to be compile-time constant, so we need to check
    that this requirement won't prevent `seed` from depending on variables.
    """
if config.list_logical_devices('TPU'):
    self.skipTest('To accommodate OSS, experimental_compile support for TPU '
                  'is not linked in.')
# GPU doesn't support int32 variables, so we use int64.
v = variables.Variable([1, 2], dtype=dtypes.int64)

@def_function.function(experimental_compile=True)
def f():
    key, counter = (
        gen_stateless_random_ops_v2.stateless_random_get_key_counter(
            seed=math_ops.cast(v.read_value(), dtypes.int32)))
    alg = gen_stateless_random_ops_v2.stateless_random_get_alg()
    exit(gen_stateless_random_ops_v2.stateless_random_normal_v2(
        shape=[], key=key, counter=counter, alg=alg))

f()
