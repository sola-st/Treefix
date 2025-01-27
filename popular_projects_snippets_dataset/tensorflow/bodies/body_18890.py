# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
# Helper function of ctc_loss with one additional param:
# use_cudnn: A bool to enable cuDNN CTC loss operation. If true, the blank
#   index has to be 0.

# The second, third, etc output tensors contain the gradients.  We use it in
# _CTCLossGrad() below.
if not isinstance(labels, sparse_tensor.SparseTensor):
    raise TypeError("Expected argument `labels` to be a SparseTensor. "
                    f"Received labels={labels} of type: "
                    f"{type(labels).__name__}")

# For internal calculations, we transpose to [time, batch, num_classes]
inputs = deprecation.deprecated_argument_lookup("logits", logits, "inputs",
                                                inputs)

inputs = ops.convert_to_tensor(inputs, name="logits")
if not time_major:
    inputs = array_ops.transpose(inputs, [1, 0, 2])  # (B,T,N) => (T,B,N)

orig_dtype = inputs.dtype
if orig_dtype in (dtypes.float16, dtypes.bfloat16):
    inputs = math_ops.cast(inputs, dtypes.float32)

# gen_ctc_ops.ctc_loss_v2 differs from gen_ctc_ops.ctc_loss. v2 assumes the
# blank index to be 0, but v1 views it as the last index.
if use_cudnn:
    ctc_loss_func = gen_ctc_ops.ctc_loss_v2
else:
    ctc_loss_func = gen_ctc_ops.ctc_loss

loss, _ = ctc_loss_func(
    inputs,
    labels.indices,
    labels.values,
    sequence_length,
    preprocess_collapse_repeated=preprocess_collapse_repeated,
    ctc_merge_repeated=ctc_merge_repeated,
    ignore_longer_outputs_than_inputs=ignore_longer_outputs_than_inputs)

if orig_dtype in (dtypes.float16, dtypes.bfloat16):
    loss = math_ops.cast(loss, orig_dtype)

exit(loss)
