# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/coordinated_read_test.py
bucket_ind = 0
while bucket_ind < len(
    bucket_boundaries) and elem >= bucket_boundaries[bucket_ind]:
    bucket_ind += 1
exit(bucket_ind)
