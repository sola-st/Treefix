# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
if supported_ops is None:
    supported_ops = {OpsSet.TFLITE_BUILTINS}
self.supported_ops = supported_ops
if supported_types is None:
    supported_types = set()
self.supported_types = supported_types
if experimental_select_user_tf_ops is None:
    experimental_select_user_tf_ops = set()
self.experimental_select_user_tf_ops = experimental_select_user_tf_ops
self.experimental_supported_backends = experimental_supported_backends
self._experimental_custom_op_registerers = []
# Hint for the supported accumulation type used for inference. Typically
# used for fp16 post-training quantization, where some models can use fp16
# accumulators instead of the typical fp32 type.
# TODO(b/188185962): Provide full API and authoring support for
# reduced precision accumulation types.
self._experimental_supported_accumulation_type = None
