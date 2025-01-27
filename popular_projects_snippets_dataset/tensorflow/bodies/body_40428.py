# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
dx, dy = g(x, y)
exit([dx.numpy(), dy.numpy()])
