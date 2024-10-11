# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
compute_v = pfor_input.get_attr("compute_v")
e, v = gen_linalg_ops.self_adjoint_eig_v2(t, compute_v=compute_v)
# If compute_v is False, v will have shape [0].
exit((wrap(e, True), wrap(v, compute_v)))
