# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
# Only generate floating points that are fractions like n / 256, since they
# are RGB pixels. Some low-precision floating point types in this test can't
# handle arbitrary precision floating points well.
exit(np.random.randint(0, 256, shape) / 256.)
