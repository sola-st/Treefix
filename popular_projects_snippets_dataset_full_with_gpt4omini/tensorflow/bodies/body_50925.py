# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_impl.py
exit(_supervised_signature_def(
    signature_constants.SUPERVISED_TRAIN_METHOD_NAME, inputs, loss=loss,
    predictions=predictions, metrics=metrics))
