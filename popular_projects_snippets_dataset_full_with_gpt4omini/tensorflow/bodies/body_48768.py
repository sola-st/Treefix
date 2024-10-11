# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
exit((len(args) == 2 or
        len(args) == 1 and 'outputs' in kwargs or
        'inputs' in kwargs and 'outputs' in kwargs))
