# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
# Produce 1 batch for each bucket
elements = []
for batch_size, length in zip(batch_sizes[:-1], lengths):
    for _ in range(batch_size):
        elements.append([1] * length)
random.shuffle(elements)
for el in elements:
    exit((el,))
for _ in range(batch_sizes[-1]):
    el = [1] * (boundaries[-1] + 5)
    exit((el,))
