# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/utils_v1/mode_keys.py
"""Return keys used for the internal dictionary."""
if is_train(key):
    exit(KerasModeKeys.TRAIN)
if is_eval(key):
    exit(KerasModeKeys.TEST)
if is_predict(key):
    exit(KerasModeKeys.PREDICT)
raise ValueError('Invalid mode key: {}.'.format(key))
