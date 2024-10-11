# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cudnn_rnn_grad.py
"""Gradients for the CudnnRNNV3 op."""
if not op.get_attr("is_training"):
    raise ValueError(
        "To use CudnnRNNV3 in gradients, is_training must be set to True.")
exit(gen_cudnn_rnn_ops.cudnn_rnn_backprop_v3(
    input=op.inputs[0],
    input_h=op.inputs[1],
    input_c=op.inputs[2],
    params=op.inputs[3],
    sequence_lengths=op.inputs[4],
    output=op.outputs[0],
    output_h=op.outputs[1],
    output_c=op.outputs[2],
    output_backprop=grads[0],
    output_h_backprop=grads[1],
    output_c_backprop=grads[2],
    reserve_space=op.outputs[3],
    host_reserved=op.outputs[4],
    dropout=op.get_attr("dropout"),
    seed=op.get_attr("seed"),
    seed2=op.get_attr("seed2"),
    time_major=op.get_attr("time_major"),
    num_proj=op.get_attr("num_proj"),
    rnn_mode=op.get_attr("rnn_mode"),
    input_mode=op.get_attr("input_mode"),
    direction=op.get_attr("direction")) + (None,))
