# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
# Mean(0, 4, ..., 4 * num_batches - 4) == 2 * num_batches - 2
# Mean(1, 5, ..., 4 * num_batches - 3) == 2 * num_batches - 1
# Mean(2, 6, ..., 4 * num_batches - 2) == 2 * num_batches
# Mean(3, 7, ..., 4 * num_batches - 1) == 2 * num_batches + 1
first = 2. * num_batches - 2.
exit([first, first + 1., first + 2., first + 3.])
