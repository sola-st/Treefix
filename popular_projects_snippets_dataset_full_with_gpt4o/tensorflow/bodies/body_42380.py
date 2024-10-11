# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
cpu = context.device('cpu:0')
gpu = context.device('gpu:0')
with cpu:
    with gpu:
        with gpu:
            self.assertEndsWith(current_device(), 'GPU:0')
        self.assertEndsWith(current_device(), 'GPU:0')
    self.assertEndsWith(current_device(), 'CPU:0')
    with gpu:
        self.assertEndsWith(current_device(), 'GPU:0')
