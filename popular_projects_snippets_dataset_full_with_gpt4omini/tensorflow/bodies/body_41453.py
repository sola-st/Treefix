# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with ops.device('GPU:0'):
    exit(gen_random_ops.random_standard_normal(
        shape, dtype=dtype, seed=seed1, seed2=seed2))
