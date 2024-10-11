# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Helper function for on_{train|test|predict}_begin methods."""
if mode == ModeKeys.TRAIN:
    self.on_train_begin()
elif mode == ModeKeys.TEST:
    self.on_test_begin()
else:
    self.on_predict_begin()
