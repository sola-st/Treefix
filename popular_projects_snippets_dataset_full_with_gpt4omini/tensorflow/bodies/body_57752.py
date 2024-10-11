# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring.py
"""Parses the given legacy ConverterError for OSS."""
for line in str(err).splitlines():
    # Check custom op usage error.
    if line.startswith(_CUSTOM_OPS_HDR):
        custom_ops = line[len(_CUSTOM_OPS_HDR):]
        err_string = (
            f"{_AUTHORING_ERROR_HDR}: op '{custom_ops}' is(are) not natively "
            "supported by TensorFlow Lite. You need to provide a custom "
            "operator. https://www.tensorflow.org/lite/guide/ops_custom")
        self._log(err_string)
    # Check TensorFlow op usage error.
    elif line.startswith(_TF_OPS_HDR):
        tf_ops = line[len(_TF_OPS_HDR):]
        err_string = (
            f"{_AUTHORING_WARNING_HDR}: op '{tf_ops}' require(s) \"Select TF "
            "Ops\" for model conversion for TensorFlow Lite. "
            "https://www.tensorflow.org/lite/guide/ops_select")
        self._log(err_string)
