# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Helper function for on_{train|test|predict}_end methods."""
if mode == ModeKeys.TRAIN:
    self.on_train_end()
elif mode == ModeKeys.TEST:
    self.on_test_end()
else:
    self.on_predict_end()
