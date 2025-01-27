# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Test case for TF-TRT conversion using Grappler directly."""

conversion_params = trt_convert.DEFAULT_TRT_CONVERSION_PARAMS._replace(
    precision_mode=trt_convert.TrtPrecisionMode.FP32)
config = self._GetConfigProto(
    rewriter_config=trt_convert.get_tensorrt_rewriter_config(
        conversion_params,
        is_dynamic_op=False,
        max_batch_size=1,
        is_v2=False))

with ops.Graph().as_default():
    # Online conversion requires a frozen graph, so we reuse inp1 as the var
    # argument.
    inp1 = array_ops.placeholder(
        dtype=dtypes.float32, shape=[None, 1, 1], name="input1")
    inp2 = array_ops.placeholder(
        dtype=dtypes.float32, shape=[None, 1, 1], name="input2")
    if device:
        with ops.device(device):
            TrtConvertTest._GetGraph(inp1, inp2, inp1)
    else:
        TrtConvertTest._GetGraph(inp1, inp2, inp1)
    with self.session(config=config) as sess:
        self._TestRun(sess, batch_size=1)
