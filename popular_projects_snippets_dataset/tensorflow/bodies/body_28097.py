# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
# Produce 1 batch for each bucket
elements = []
for bucket_elements, length in zip(n_bucket_elements, lengths):
    # Using only full sequences (opposed to the strategy employed in
    # `testBucket`) makes checking the sum a lot easier.
    record_len = length
    for _ in range(bucket_elements):
        elements.append([1] * record_len)
random.shuffle(elements)
for el in elements:
    exit((_format_record(el, sparse),))
