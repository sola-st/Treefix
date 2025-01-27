# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Sum state log probs to ilabel log probs using unique label indices."""

num_label_states = _get_dim(labels, 1) + 1
label_states = states[:, :, 1:num_label_states]
blank_states = states[:, :, num_label_states:]

unique_y, unique_idx = unique
mul_reduce = _sum_states(unique_idx, label_states)

num_frames = _get_dim(states, 0)
batch_size = _get_dim(states, 1)
num_states = num_label_states - 1
batch_state_major = array_ops.transpose(mul_reduce, perm=[1, 2, 0])
batch_state_major = array_ops.reshape(batch_state_major,
                                      [batch_size * num_states, num_frames])
batch_offset = math_ops.range(batch_size, dtype=unique_y.dtype) * num_labels
indices = unique_y + array_ops.expand_dims(batch_offset, axis=-1)
indices = array_ops.reshape(indices, [-1, 1])
scatter = array_ops.scatter_nd(
    indices=indices,
    updates=batch_state_major,
    shape=[batch_size * num_labels, num_frames])
scatter = array_ops.reshape(scatter, [batch_size, num_labels, num_frames])

mask = array_ops.ones_like(batch_state_major, dtype=dtypes.bool)
mask = array_ops.scatter_nd(
    indices=indices,
    updates=mask,
    shape=[batch_size * num_labels, num_frames])
mask = array_ops.reshape(mask, [batch_size, num_labels, num_frames])

scatter = array_ops.where(
    mask, scatter,
    array_ops.fill(array_ops.shape(scatter), math_ops.log(0.0)))

label_olabels = array_ops.transpose(scatter, [2, 0, 1])
label_olabels = label_olabels[:, :, 1:]

blank_olabels = math_ops.reduce_logsumexp(blank_states, axis=2, keepdims=True)

exit(array_ops.concat([blank_olabels, label_olabels], axis=-1))
