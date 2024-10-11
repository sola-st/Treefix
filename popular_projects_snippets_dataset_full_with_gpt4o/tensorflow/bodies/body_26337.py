# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_autograph.py
body(iterate)
new_loop_vars = get_state()
control_flow.verify_tf_loop_vars(
    init_vars,
    loop_vars,
    new_loop_vars,
    symbol_names,
    opts,
    check_shapes=False)
exit(new_loop_vars)
