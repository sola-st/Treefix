# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
input_data = [float("nan")] * 16
output_backprop = [
    float("nan"), 12.0, 13.0, 15.0,
    float("nan"), 17.0, 19.0, 20.0,
    float("nan")
]
# Test the CPU implementation, which propagates diffs in case of NaN
expected_input_backprop_tf_cpu = [
    float("nan"), 12.0, 13.0, 0.0, 15.0,
    float("nan"), 17.0, 0.0, 19.0, 20.0,
    float("nan"), 0.0, 0.0, 0.0, 0.0, 0.0
]
for v2 in [True, False]:
    self._testMaxPoolGradDirect(
        input_data,
        output_backprop,
        expected_input_backprop_tf_cpu,
        input_sizes=[1, 4, 4, 1],
        output_sizes=[1, 3, 3, 1],
        window_rows=2,
        window_cols=2,
        row_stride=1,
        col_stride=1,
        padding="VALID",
        use_gpu=False,
        v2=v2)

if not test.is_gpu_available():
    exit()

# The functionality associated with TF_ENABLE_NANPROP is currently
# not supported on the ROCm platform, so skip this part of the test
# NANs in input lead to non-deterministic results, and hence skipping
# the remaining tests altogether on the ROCm platform
if test.is_built_with_rocm():
    exit()

# Test the GPU implementation that uses cudnn for now.
saved_nanprop = os.environ.get("TF_ENABLE_MAXPOOL_NANPROP")
# Do not propagate the diff in cases of NaNs
os.environ["TF_ENABLE_MAXPOOL_NANPROP"] = "0"
expected_input_backprop_cudnn = [
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0
]

for v2 in [True, False]:
    self._testMaxPoolGradDirect(
        input_data,
        output_backprop,
        expected_input_backprop_cudnn,
        input_sizes=[1, 4, 4, 1],
        output_sizes=[1, 3, 3, 1],
        window_rows=2,
        window_cols=2,
        row_stride=1,
        col_stride=1,
        padding="VALID",
        use_gpu=True,
        v2=v2)

# Propagate the diff in cases of NaNs
os.environ["TF_ENABLE_MAXPOOL_NANPROP"] = "1"
expected_input_backprop_cudnn = expected_input_backprop_tf_cpu

for v2 in [True, False]:
    self._testMaxPoolGradDirect(
        input_data,
        output_backprop,
        expected_input_backprop_cudnn,
        input_sizes=[1, 4, 4, 1],
        output_sizes=[1, 3, 3, 1],
        window_rows=2,
        window_cols=2,
        row_stride=1,
        col_stride=1,
        padding="VALID",
        use_gpu=True,
        v2=v2)

if saved_nanprop:
    os.environ["TF_ENABLE_MAXPOOL_NANPROP"] = saved_nanprop
else:
    del os.environ["TF_ENABLE_MAXPOOL_NANPROP"]
