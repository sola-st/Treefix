# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
shape = [2, 3, 4, 3, 4]
x = np.random.uniform(size=shape) + 1j * np.random.uniform(size=shape)

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    exit(op_func(x_i))

self._test_loop_fn(loop_fn, 2)
