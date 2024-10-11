# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
mean = np.mean(x_np, (1, 2), keepdims=True)
y_np = mean + contrast_factor * (x_np - mean)
exit(y_np)
