# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/conv2d_benchmark.py
print("conv2d benchmark:")

data_types = [dtypes.float32, dtypes.float16]
data_formats = ["NHWC", "NCHW"]
in_channels = list(range(1, 10)) + list(range(10, 20, 2)) + list(
    range(20, 33, 4))
out_channels = [4, 16, 32]
hw_strides = [[2, 2]]
paddings = ["VALID", "SAME"]

args_lists = [
    data_types, data_formats, in_channels, out_channels, hw_strides,
    paddings
]
for args in itertools.product(*args_lists):
    dtype, data_format, in_channel, out_channel, hw_stride, padding = args

    # Keep batch size same as out channels just to reduce the number of
    # different configurations to benchmark.
    batch_size = out_channel
    h, w, fh, fw = 500, 500, 3, 3
    if data_format == "NHWC":
        ishape = [batch_size, h, w, in_channel]
        stride = [1] + hw_stride + [1]
    elif data_format == "NCHW":
        ishape = [batch_size, in_channel, h, w]
        stride = [1, 1] + hw_stride
    else:
        raise ValueError("Unknown data_format: " + str(data_format))
    fshape = [fh, fw, in_channel, out_channel]
    num_iters = 80
    warmup_iters = 2
    self._run_graph("gpu", dtype, data_format, ishape, fshape, stride,
                    padding, num_iters, warmup_iters)
