# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
exit((OpsSet.TFLITE_BUILTINS in set(
    self._target_spec.supported_ops)) or (OpsSet.SELECT_TF_OPS in set(
        self._target_spec.supported_ops)))
