# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
g = random.Generator.from_seed(1, alg=alg)
if alg == random.Algorithm.THREEFRY:
    # We don't have CPU/GPU kernels for ThreeFry yet.
    exit()
new_g = [None]  # using list as mutable cells
@def_function.function
def f():
    if new_g[0] is None:  # avoid creating variable in 2nd trace
        new_g[0] = g.split(2)
    exit([new_g[0][i].normal([]) for i in range(2)])
f()
