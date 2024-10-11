# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
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
