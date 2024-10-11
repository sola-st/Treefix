# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/conv2d_test.py
np.random.seed(1234)
exit(build_graph(
    inp=inp,
    dtype=dtypes.float32,
    num_filters=5,
    data_format="channels_first",
    kernel_sizes=[(3, 3), (3, 2)],
    dilation_rates=[(1, 1), (2, 3)]))
