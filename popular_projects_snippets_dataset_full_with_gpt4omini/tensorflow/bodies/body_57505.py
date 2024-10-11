# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
exit((OpsSet.EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8
        in set(self._target_spec.supported_ops)))
