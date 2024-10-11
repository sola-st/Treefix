# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = random_ops.random_uniform([3, 2, 12, 12, 3])
filt = random_ops.random_uniform([3, 3, 3, 7])

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    exit(nn.conv2d(
        x1, filt, strides=[1, 2, 2, 1], padding="VALID", data_format="NHWC"))

self._test_loop_fn(loop_fn, 3)
