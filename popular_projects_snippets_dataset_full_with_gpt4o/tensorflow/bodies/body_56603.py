# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Initializes debugger options.

    Args:
      layer_debug_metrics: a dict to specify layer debug functions
        {function_name_str: function} where the function accepts result of
          NumericVerify Op, which is value difference between float and
          dequantized op results. The function returns single scalar value.
      model_debug_metrics: a dict to specify model debug functions
        {function_name_str: function} where the function accepts outputs from
          two models, and returns single scalar value for a metric. (e.g.
          accuracy, IoU)
      layer_direct_compare_metrics: a dict to specify layer debug functions
        {function_name_str: function}. The signature is different from that of
          `layer_debug_metrics`, and this one gets passed (original float value,
          original quantized value, scale, zero point). The function's
          implementation is responsible for correctly dequantize the quantized
          value to compare. Use this one when comparing diff is not enough.
          (Note) quantized value is passed as int8, so cast to int32 is needed.
      denylisted_ops: a list of op names which is expected to be removed from
        quantization.
      denylisted_nodes: a list of op's output tensor names to be removed from
        quantization.
      fully_quantize: Bool indicating whether to fully quantize the model.
        Besides model body, the input/output will be quantized as well.
        Corresponding to mlir_quantize's fully_quantize parameter.

    Raises:
      ValueError: when there are duplicate keys
    """
self.layer_debug_metrics = layer_debug_metrics
self.model_debug_metrics = model_debug_metrics
self.layer_direct_compare_metrics = layer_direct_compare_metrics

keys = []
for metrics in [
    layer_debug_metrics, model_debug_metrics, layer_direct_compare_metrics
]:
    if metrics is not None:
        keys.extend(metrics.keys())
if len(keys) != len(set(keys)):
    raise ValueError('Provided metrics have duplicate keys.')

self.denylisted_ops = denylisted_ops
self.denylisted_nodes = denylisted_nodes
self.fully_quantize = fully_quantize
