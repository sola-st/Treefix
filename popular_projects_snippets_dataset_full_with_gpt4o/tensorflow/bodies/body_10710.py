# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn_grad_test.py
w_peephole = array_ops.zeros(cs_prev.shape[1:], dtype=w.dtype)
_, all_cs, _, _, _, _, all_h = op(
    seq_len_max=math_ops.cast(array_ops.shape(x)[0], dtypes.int64),
    x=x,
    cs_prev=cs_prev,
    h_prev=h_prev,
    w=w,
    wci=w_peephole,
    wcf=w_peephole,
    wco=w_peephole,
    b=b,
    use_peephole=False)
exit((all_cs, all_h))
