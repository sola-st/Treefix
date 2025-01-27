# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Helper function initializes stats."""
# TODO(b/177749613) : Fix the dependency on tf.lite._get_ops_details()
# Following code is needed to get op's name from the output tensor index,
# since NumericVerify op only provides its quantized input tensor index.
self._defining_op = dict()
for op_info in self._quant_interpreter._get_ops_details():  # pylint: disable=protected-access
    self._defining_op.update(
        {tensor_idx: op_info['index'] for tensor_idx in op_info['outputs']})

self._numeric_verify_tensor_details = None
self._numeric_verify_op_details = None
if not self._get_numeric_verify_tensor_details():
    raise ValueError('Please check if the quantized model is in debug mode')

self._layer_debug_metrics = _DEFAULT_LAYER_DEBUG_METRICS.copy()
if self._debug_options.layer_debug_metrics:
    self._layer_debug_metrics.update(self._debug_options.layer_debug_metrics)

self.layer_statistics = None
self.model_statistics = None

self._metrics = metrics_stub.TFLiteMetrics()
self._metrics.increase_counter_debugger_creation()
