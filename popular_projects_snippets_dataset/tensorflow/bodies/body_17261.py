# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Test deterministic randomness in jpeg quality by checking that the same
# sequence of jpeg quality adjustments are returned each round given the
# same seed.
with test_util.use_gpu():
    path = ("tensorflow/core/lib/jpeg/testdata/medium.jpg")
    jpeg = io_ops.read_file(path)
    image = image_ops.decode_jpeg(jpeg)
    jpeg_quality = (40, 100)
    seeds_list = [(1, 2), (3, 4)]

    iterations = 2
    random_jpeg_images_all = [[] for _ in range(iterations)]
    for random_jpeg_images in random_jpeg_images_all:
        for seed in seeds_list:
            distorted_jpeg = image_ops.stateless_random_jpeg_quality(
                image, jpeg_quality[0], jpeg_quality[1], seed=seed)
            # Verify that the random jpeg image is different from the original
            # jpeg image.
            self.assertNotAllEqual(image, distorted_jpeg)
            random_jpeg_images.append(self.evaluate(distorted_jpeg))

      # Verify that the results are identical given the same seed.
    for i in range(1, iterations):
        self.assertAllEqual(random_jpeg_images_all[0],
                            random_jpeg_images_all[i])
