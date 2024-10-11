# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
height = 40
width = 50
x_shape = [height, width, 1]
image = np.zeros(x_shape, dtype=np.int32)

# Create an object with 1's in a region with area A and require that
# the total pixel values >= 0.1 * A.
min_object_covered = 0.1

xmin = 2
ymin = 3
xmax = 12
ymax = 13
for x in np.arange(xmin, xmax + 1, 1):
    for y in np.arange(ymin, ymax + 1, 1):
        image[x, y] = 1

    # Bounding box is specified as (ymin, xmin, ymax, xmax) in
    # relative coordinates.
bounding_box = (float(ymin) / height, float(xmin) / width,
                float(ymax) / height, float(xmax) / width)

self._testSampleDistortedBoundingBox(
    image,
    bounding_box=bounding_box,
    min_object_covered=min_object_covered,
    aspect_ratio_range=(0.75, 1.33),
    area_range=(0.05, 1.0))
