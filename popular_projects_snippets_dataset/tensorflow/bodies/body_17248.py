# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Build a simple color ramp RGB image."""
w, h = 256, 200
i = np.arange(h)[:, None]
j = np.arange(w)
image = np.empty((h, w, 3), dtype=np.uint8)
image[:, :, 0] = i
image[:, :, 1] = j
image[:, :, 2] = (i + j) >> 1
exit(image)
