# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
devices = context.context().devices()
exit(len([d for d in devices if 'device:TPU:' in d]) > 1)
