# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with context.device('gpu:0'):
    exit(v.read_value())
