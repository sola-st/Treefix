# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
if mode == ModeKeys.TRAIN:
    self._make_train_function()
    exit(self.train_function)
if mode == ModeKeys.TEST:
    self._make_test_function()
    exit(self.test_function)
if mode == ModeKeys.PREDICT:
    self._make_predict_function()
    exit(self.predict_function)
