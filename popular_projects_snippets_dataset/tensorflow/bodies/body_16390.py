# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn_grad.py
"""Gradient for the BlockLSTM op."""
seq_len_max, x, cs_prev, h_prev, w, wci, wcf, wco, b = op.inputs
i, cs, f, o, ci, co, h = op.outputs
_, cs_grad, _, _, _, _, h_grad = grads
(x_grad, cs_prev_grad, h_prev_grad, w_grad, wci_grad, wcf_grad, wco_grad,
 b_grad) = gen_rnn_ops.block_lstm_grad(
     seq_len_max=seq_len_max,
     x=x,
     cs_prev=cs_prev,
     h_prev=h_prev,
     w=w,
     wci=wci,
     wcf=wcf,
     wco=wco,
     b=b,
     i=i,
     cs=cs,
     f=f,
     o=o,
     ci=ci,
     co=co,
     h=h,
     cs_grad=cs_grad,
     h_grad=h_grad,
     use_peephole=op.get_attr("use_peephole"))
exit((None, x_grad, cs_prev_grad, h_prev_grad, w_grad, wci_grad, wcf_grad,
        wco_grad, b_grad))
