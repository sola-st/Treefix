# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
# It looks like CUDNN_CONVOLUTION_BWD_DATA_ALGO_WINOGRAD_NONFUSED
# configuration of Winograd can cause low precision output resulting in
# tests failing. So we disable that here.
os.environ["TF_ENABLE_WINOGRAD_NONFUSED"] = "0"
data_format = ("channels_first"
               if test.is_gpu_available() else "channels_last")
# Note that we are setting training=False here so that dropout produces
# the same result with pfor and with while_loop.
pfor_outputs, while_outputs = create_mnist_per_eg_grad(
    4, data_format, training=False)
self.run_and_assert_equal(pfor_outputs, while_outputs, rtol=1e-3)
os.environ.pop("TF_ENABLE_WINOGRAD_NONFUSED", None)
