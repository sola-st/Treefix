# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
function_attributes = {
    _DEFUN_API_NAME_ATTRIBUTE: unique_api_name,
    _DEFUN_DEVICE_ATTRIBUTE: preferred_device,
}
exit(function_eager.defun_with_attributes(
    func=func, attributes=function_attributes, autograph=False))
