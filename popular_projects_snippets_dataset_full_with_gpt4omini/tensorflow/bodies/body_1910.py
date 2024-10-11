# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
self.assertEqual(x_np.shape[-1], 3)
x_v = x_np.reshape([-1, 3])
y_v = np.ndarray(x_v.shape, dtype=x_v.dtype)
channel_count = x_v.shape[0]
for i in range(channel_count):
    r = x_v[i][0]
    g = x_v[i][1]
    b = x_v[i][2]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    s *= scale
    s = min(1.0, max(0.0, s))
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    y_v[i][0] = r
    y_v[i][1] = g
    y_v[i][2] = b
exit(y_v.reshape(x_np.shape))
