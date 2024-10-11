# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
# Produce 1 batch for each bucket
elements = []
for batch_size, length in zip(batch_sizes, lengths):
    record_len = length - 1
    for _ in range(batch_size):
        elements.append([1] * record_len)
        record_len = length
random.shuffle(elements)
for el in elements:
    exit((_format_record(el, sparse),))
