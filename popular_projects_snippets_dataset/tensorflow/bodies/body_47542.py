# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
function_attributes = {
    _FUNCTION_API_NAME_ATTRIBUTE: unique_api_name,
    _FUNCTION_DEVICE_ATTRIBUTE: preferred_device,
}
function_attributes.update(supportive_attributes)
exit(function.defun_with_attributes(func=func,
                                      attributes=function_attributes,
                                      autograph=False))
