# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
exit((OpsSet.TFLITE_BUILTINS_INT8 in set(
    self._target_spec.supported_ops)) or (set(
        self._target_spec.supported_types) == set([_dtypes.int8])))
