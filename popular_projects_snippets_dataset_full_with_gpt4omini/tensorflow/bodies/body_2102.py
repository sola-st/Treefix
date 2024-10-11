# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lrn_ops_test.py
"""Compute expected result."""
output = copy.deepcopy(input_image)
batch_size = input_image.shape[0]
rows = input_image.shape[1]
cols = input_image.shape[2]
depth = input_image.shape[3]
for b in range(batch_size):
    for r in range(rows):
        for c in range(cols):
            for d in range(depth):
                begin = max(0, d - lrn_depth_radius)
                end = min(depth, d + lrn_depth_radius + 1)
                patch = input_image[b, r, c, begin:end]
                output[b, r, c, d] /= (
                    np.power(bias + alpha * np.sum(patch * patch), beta))
exit(output)
