# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
"""Computes actual batch outputs of dataset and stores in a set."""
batch = self.getNext(dataset)
all_sparse_tensors = set()
with self.assertRaises(errors.OutOfRangeError):
    while True:
        output = self.evaluate(batch())
        sprs_tensor = (tuple([tuple(idx) for idx in output.indices]),
                       tuple(output.values))
        all_sparse_tensors.add(sprs_tensor)

exit(all_sparse_tensors)
