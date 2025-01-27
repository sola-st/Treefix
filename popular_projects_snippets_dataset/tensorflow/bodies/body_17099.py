# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
num_pixels = np.prod(x.shape)
mn = np.mean(x)
std = np.std(x)
stddev = max(std, 1.0 / math.sqrt(num_pixels))

y = x.astype(np.float32)
y -= mn
y /= stddev
exit(y)
