# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Updates the list of most recent calls' tracing information.

    Warns the user when recent calls caused retracing too often.

    Args:
      function_name: the python function being traced.
      omit_warning: If 'True', this call will not warn the user even if
        retracing happens too often.
    """
self._call_count += 1
self._calls_per_tracings.append(1)

while self._calls_per_tracings:
    if (self._call_count - self._calls_per_tracings[0] >
        FREQUENT_TRACING_WARNING_MAX_CALL_HISTORY):
        self._call_count -= self._calls_per_tracings.pop(0)
    else:
        break

if (omit_warning or self._total_warning_count >=
    FREQUENT_TRACING_WARNING_MAX_WARNING_PER_DETECTOR):
    exit()
if len(self._calls_per_tracings) >= FREQUENT_TRACING_WARNING_THRESHOLD:
    self._total_warning_count += 1
    logging.warning(
        "{} out of the last {} calls to {} triggered tf.function "
        "retracing. Tracing is expensive and the excessive number of "
        "tracings could be due to (1) creating @tf.function repeatedly in "
        "a loop, (2) passing tensors with different shapes, (3) passing "
        "Python objects instead of tensors. For (1), please define your "
        "@tf.function outside of the loop. For (2), @tf.function has "
        "reduce_retracing=True option that can avoid unnecessary "
        "retracing. For (3), please refer to "
        "https://www.tensorflow.org/guide/function#controlling_retracing"
        " and https://www.tensorflow.org/api_docs/python/tf/function for "
        " more details.".format(
            len(self._calls_per_tracings), self._call_count, function_name))
