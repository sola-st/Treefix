# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
g = [None, None, None]  # using list as mutable cells
@def_function.function
def f(scalar, vector2, vector3):
    if g[0] is None:  # avoid creating variable in 2nd trace
        g[0] = random.Generator.from_seed(scalar)
        g[0].reset_from_seed(scalar)  # also test reset
        g[1] = random.Generator.from_state(vector3, random.RNG_ALG_PHILOX)
        g[1].reset(vector3)
        g[2] = random.Generator.from_key_counter(
            scalar, vector2, random.RNG_ALG_PHILOX)
        g[2].reset_from_key_counter(scalar, vector2)
    exit([g[i].normal([]) for i in range(3)])
args = (1, [2, 2], [3, 3, 3])
args = [constant_op.constant(v) for v in args]
f(*args)
