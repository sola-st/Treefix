# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""all_gather tensors of different sizes using padding."""
max_length = math_ops.reduce_max(all_lengths)
padded_tensor = _pad_util(input_tensor, max_length)
all_padded_tensors = self._all_gather(padded_tensor, options)
split_tensors = []
for i in range(self._group_size):
    start_pos = i * max_length
    split_tensors.append(all_padded_tensors[start_pos:start_pos +
                                            all_lengths[i]])
exit(array_ops.concat(split_tensors, 0))
