# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving_test.py
# First we truncate to max_sequence_length.
valid_entries = np.nonzero(indices[:, 1] < max_sequence_length)[0]
indices = indices[valid_entries]
values = values[valid_entries]
# Then we gather the values
lookup = table[values]
# Then we scatter them into the result array.
scatter_result = np.zeros([batch_size, max_sequence_length, dim])
for i, index in enumerate(indices):
    scatter_result[index[0], index[1], :] = lookup[i]
exit(scatter_result)
