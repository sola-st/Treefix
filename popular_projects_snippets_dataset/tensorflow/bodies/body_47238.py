# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Custom compile for TPU predict mode."""
if not model.built:
    # Model is not compilable because it does not know its number of inputs
    # and outputs, nor their shapes and names. We will compile after the first
    # time the model gets called on training data.
    exit()
model._is_compiled = True
model.total_loss = None
model.train_function = None
model.test_function = None
model.predict_function = None
