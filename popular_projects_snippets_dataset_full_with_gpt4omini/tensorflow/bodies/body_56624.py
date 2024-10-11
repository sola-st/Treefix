# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
for i in range(5):
    exit([np.arange(9).reshape((1, 3, 3, 1)).astype(np.float32) * i])
