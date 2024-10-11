# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Test the total variation for a few handmade examples."""

# We create an image that is 2x2 pixels with 3 color channels.
# The image is very small so we can check the result by hand.

# Red color channel.
# The following are the sum of absolute differences between the pixels.
# sum row dif = (4-1) + (7-2) = 3 + 5 = 8
# sum col dif = (2-1) + (7-4) = 1 + 3 = 4
r = [[1, 2], [4, 7]]

# Blue color channel.
# sum row dif = 18 + 29 = 47
# sum col dif = 7 + 18 = 25
g = [[11, 18], [29, 47]]

# Green color channel.
# sum row dif = 120 + 193 = 313
# sum col dif = 47 + 120 = 167
b = [[73, 120], [193, 313]]

# Combine the 3 color channels into a single 3-dim array.
# The shape is (2, 2, 3) corresponding to (height, width and color).
a = np.dstack((r, g, b))

# Total variation for this image.
# Sum of all pixel differences = 8 + 4 + 47 + 25 + 313 + 167 = 564
tot_var = 564

# Calculate the total variation using TensorFlow and assert it is correct.
self._test(a, tot_var)

# If we add 1 to all pixel-values then the total variation is unchanged.
self._test(a + 1, tot_var)

# If we negate all pixel-values then the total variation is unchanged.
self._test(-a, tot_var)  # pylint: disable=invalid-unary-operand-type

# Scale the pixel-values by a float. This scales the total variation as
# well.
b = 1.1 * a
self._test(b, 1.1 * tot_var)

# Scale by another float.
c = 1.2 * a
self._test(c, 1.2 * tot_var)

# Combine these 3 images into a single array of shape (3, 2, 2, 3)
# where the first dimension is for the image-number.
multi = np.vstack((a[np.newaxis, :], b[np.newaxis, :], c[np.newaxis, :]))

# Check that TensorFlow correctly calculates the total variation
# for each image individually and returns the correct array.
self._test(multi, tot_var * np.array([1.0, 1.1, 1.2]))
