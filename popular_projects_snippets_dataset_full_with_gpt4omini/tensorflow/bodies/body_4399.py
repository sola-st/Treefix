# Extracted from ./data/repos/tensorflow/tensorflow/c/experimental/saved_model/internal/testdata/gen_saved_models.py
acc, _ = control_flow_ops.while_loop(
    cond=lambda acc, i: i > 0,
    body=lambda acc, i: (acc + i, i - 1),
    loop_vars=(constant_op.constant(0.0), value))
exit(acc)
