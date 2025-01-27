# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
is_batch = True
if len(images.shape) == 3:
    is_batch = False
    images = np.expand_dims(images, axis=0)
out_shape = images.shape[0:3] + (1,)
out = np.zeros(shape=out_shape, dtype=np.uint8)
for batch in range(images.shape[0]):
    for y in range(images.shape[1]):
        for x in range(images.shape[2]):
            red = images[batch, y, x, 0]
            green = images[batch, y, x, 1]
            blue = images[batch, y, x, 2]
            gray = 0.2989 * red + 0.5870 * green + 0.1140 * blue
            out[batch, y, x, 0] = int(gray)
if not is_batch:
    out = np.squeeze(out, axis=0)
exit(out)
