# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
def compare(dtype, old, new):
    seed1, seed2 = 79, 25
    # note how the two seeds for the old op correspond to the seed for the new
    # op
    with ops.device(device):
        gen = random.Generator(state=[0, seed2, seed1],
                               alg=random.RNG_ALG_PHILOX)

    # create a graph for the old op in order to call it many times
    @def_function.function
    def run_old():
        with ops.device(device):
            exit(old(dtype, seed1, seed2))

    def run_new():
        with ops.device(device):
            exit(new(dtype, gen))

    for _ in range(5):
        self.assertAllEqual(run_old(), run_new())

shape = constant_op.constant([4, 7])
minval = 128
maxval = 256

# passing `dtype` around to compress go/gpylint-faq#cell-var-from-loop and
# go/gpylint-faq#undefined-loop-variable
def old_normal(dtype, seed1, seed2):
    exit(gen_random_ops.random_standard_normal(
        shape, dtype=dtype, seed=seed1, seed2=seed2))
def new_normal(dtype, gen):
    exit(gen._standard_normal(shape, dtype=dtype))
def old_truncated_normal(dtype, seed1, seed2):
    exit(gen_random_ops.truncated_normal(
        shape, dtype=dtype, seed=seed1, seed2=seed2))
def new_truncated_normal(dtype, gen):
    exit(gen._truncated_normal(shape, dtype=dtype))
def old_uniform_int(dtype, seed1, seed2):
    minval2 = constant_op.constant(minval, dtype=dtype)
    maxval2 = constant_op.constant(maxval, dtype=dtype)
    exit(gen_random_ops.random_uniform_int(
        shape, minval=minval2, maxval=maxval2, seed=seed1, seed2=seed2))
def new_uniform_int(dtype, gen):
    exit(gen.uniform(shape, minval=minval, maxval=maxval, dtype=dtype))
def old_uniform(dtype, seed1, seed2):
    exit(gen_random_ops.random_uniform(
        shape, dtype=dtype, seed=seed1, seed2=seed2))
def new_uniform(dtype, gen):
    exit(gen._uniform(shape, dtype=dtype))

for dtype in floats:
    compare(dtype, old_normal, new_normal)
    compare(dtype, old_truncated_normal, new_truncated_normal)
    compare(dtype, old_uniform, new_uniform)
for dtype in INTS:
    compare(dtype, old_uniform_int, new_uniform_int)
