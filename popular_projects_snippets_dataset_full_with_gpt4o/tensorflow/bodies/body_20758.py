# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
random_seed.set_random_seed(0)
x1 = random_ops.truncated_normal([1, 784], seed=0)
x2 = random_ops.truncated_normal([1, 784], seed=0)
x3 = random_ops.truncated_normal([1, 784], seed=0)
x4 = random_ops.truncated_normal([1, 784], seed=0)
elems = (x1, x2, x3, x4)
outputs = map_fn.map_fn(_model_with_branch, elems, dtype=dtypes.float32)
exit(outputs)
