# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
random_seed.set_random_seed(5)

# Trace without a batch size and number of frames
batch_size = None
num_labels = 6
label_length = 5
num_frames = None

@def_function.function
def func(labels, logits, label_lengths, logit_lengths):
    unique_labels = ctc_ops.ctc_unique_labels(labels) if unique else None
    exit(ctc_ops.ctc_loss_dense(
        labels=labels,
        logits=logits,
        label_length=label_lengths,
        logit_length=logit_lengths,
        unique=unique_labels,
        blank_index=blank_index))

labels_spec = tensor_spec.TensorSpec([batch_size, label_length],
                                     dtypes.int64)
logits_spec = tensor_spec.TensorSpec([num_frames, batch_size, num_labels],
                                     dtypes.float32)
label_lengths_spec = tensor_spec.TensorSpec([batch_size], dtypes.int64)
logit_lengths_spec = tensor_spec.TensorSpec([batch_size], dtypes.int64)

f = func.get_concrete_function(
    labels_spec, logits_spec, label_lengths_spec, logit_lengths_spec)

# Execute with a defined batch size and number of frames
batch_size = 8
num_frames = 12

logits = random_ops.random_uniform([num_frames, batch_size, num_labels])
labels = random_ops.random_uniform(
    [batch_size, label_length], minval=1, maxval=num_labels,
    dtype=dtypes.int64)

label_lengths = random_ops.random_uniform(
    [batch_size], minval=2, maxval=label_length, dtype=dtypes.int64)
label_mask = array_ops.sequence_mask(
    label_lengths, maxlen=label_length, dtype=label_lengths.dtype)
labels *= label_mask

logit_lengths = constant_op.constant(
    [num_frames] * batch_size, dtype=dtypes.int64)

f(labels, logits, label_lengths, logit_lengths)
