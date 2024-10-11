# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/accumulate_n_benchmark.py
inputs = [random_ops.random_uniform(shape=[size]) for _ in range(n)]
random.shuffle(inputs)
exit(inputs)
