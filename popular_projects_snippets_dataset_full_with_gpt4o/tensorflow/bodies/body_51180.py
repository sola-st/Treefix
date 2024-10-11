# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output.py
if len(receiver_tensors) != 1:
    raise ValueError(
        'Regression signatures can only accept a single tensor input of '
        'type tf.string. Please check to make sure that you have structured '
        'the serving_input_receiver_fn so that it creates a single string '
        'placeholder. If your model function expects multiple inputs, then '
        'use `tf.io.parse_example()` to parse the string into multiple '
        f'tensors.\n Received: {receiver_tensors}')
(_, examples), = receiver_tensors.items()
if dtypes.as_dtype(examples.dtype) != dtypes.string:
    raise ValueError(
        'Regression signatures can only accept a single tensor input of '
        'type tf.string. Please check to make sure that you have structured '
        'the serving_input_receiver_fn so that it creates a single string '
        'placeholder. If your model function expects multiple inputs, then '
        'use `tf.io.parse_example()` to parse the string into multiple '
        f'tensors.\n Received: {receiver_tensors}')
exit(signature_def_utils.regression_signature_def(examples, self.value))
