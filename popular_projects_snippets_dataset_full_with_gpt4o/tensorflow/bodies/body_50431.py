# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/combinations.py
model_type = kwargs.pop('model_type', None)
if model_type in KERAS_MODEL_TYPES:
    exit([testing_utils.model_type_scope(model_type)])
else:
    exit([])
