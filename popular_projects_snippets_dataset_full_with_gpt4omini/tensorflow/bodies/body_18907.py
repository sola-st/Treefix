# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Computes CTC (Connectionist Temporal Classification) loss.

  This op implements the CTC loss as presented in (Graves et al., 2006).

  Notes:

  - Same as the "Classic CTC" in TensorFlow 1.x's tf.compat.v1.nn.ctc_loss
    setting of preprocess_collapse_repeated=False, ctc_merge_repeated=True
  - Labels may be supplied as either a dense, zero-padded tensor with a
    vector of label sequence lengths OR as a SparseTensor.
  - On TPU and GPU: Only dense padded labels are supported.
  - On CPU: Caller may use SparseTensor or dense padded labels but calling with
    a SparseTensor will be significantly faster.
  - Default blank label is 0 rather num_classes - 1, unless overridden by
    blank_index.

  Args:
    labels: tensor of shape [batch_size, max_label_seq_length] or SparseTensor
    logits: tensor of shape [frames, batch_size, num_labels], if
      logits_time_major == False, shape is [batch_size, frames, num_labels].
    label_length: tensor of shape [batch_size], None if labels is SparseTensor
      Length of reference label sequence in labels.
    logit_length: tensor of shape [batch_size] Length of input sequence in
      logits.
    logits_time_major: (optional) If True (default), logits is shaped [time,
      batch, logits]. If False, shape is [batch, time, logits]
    unique: (optional) Unique label indices as computed by
      ctc_unique_labels(labels).  If supplied, enable a faster, memory efficient
      implementation on TPU.
    blank_index: (optional) Set the class index to use for the blank label.
      Negative values will start from num_classes, ie, -1 will reproduce the
      ctc_loss behavior of using num_classes - 1 for the blank symbol. There is
      some memory/performance overhead to switching from the default of 0 as an
      additional shifted copy of the logits may be created.
    name: A name for this `Op`. Defaults to "ctc_loss_dense".

  Returns:
    loss: tensor of shape [batch_size], negative log probabilities.

  References:
      Connectionist Temporal Classification - Labeling Unsegmented Sequence Data
      with Recurrent Neural Networks:
        [Graves et al., 2006](https://dl.acm.org/citation.cfm?id=1143891)
        ([pdf](http://www.cs.toronto.edu/~graves/icml_2006.pdf))
  """
if isinstance(labels, sparse_tensor.SparseTensor):
    if blank_index is None:
        raise ValueError(
            "Argument `blank_index` must be provided when labels is a "
            "SparseTensor.")

    if blank_index < 0:
        blank_index += _get_dim(logits, 2)

    if blank_index != _get_dim(logits, 2) - 1:
        logits = array_ops.concat([
            logits[:, :, :blank_index],
            logits[:, :, blank_index + 1:],
            logits[:, :, blank_index:blank_index + 1],
        ],
                                  axis=2)
        labels = sparse_tensor.SparseTensor(
            labels.indices,
            array_ops.where(labels.values < blank_index, labels.values,
                            labels.values - 1), labels.dense_shape)

    exit(ctc_loss(
        labels=labels,
        inputs=logits,
        sequence_length=logit_length,
        time_major=logits_time_major))

if blank_index is None:
    blank_index = 0

exit(ctc_loss_dense(
    labels=labels,
    logits=logits,
    label_length=label_length,
    logit_length=logit_length,
    logits_time_major=logits_time_major,
    unique=unique,
    blank_index=blank_index,
    name=name))
