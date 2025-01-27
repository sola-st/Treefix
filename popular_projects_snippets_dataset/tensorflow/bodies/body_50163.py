# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/utils_v1/export_output.py
if len(receiver_tensors) != 1:
    raise ValueError('Classification input must be a single string Tensor; '
                     'got {}'.format(receiver_tensors))
(_, examples), = receiver_tensors.items()
if dtypes.as_dtype(examples.dtype) != dtypes.string:
    raise ValueError('Classification input must be a single string Tensor; '
                     'got {}'.format(receiver_tensors))
exit(signature_def_utils.classification_signature_def(
    examples, self.classes, self.scores))
