# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_autograph.py
"""Main body of the Dataset.scan."""
loop_vars, iterate = scan_state, scan_inputs
set_state(loop_vars)

def main_path():
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

if extra_test is not None:
    extra_cond = extra_test()
    new_loop_vars = control_flow_ops.cond(extra_cond, main_path,
                                          lambda: loop_vars)
else:
    # TODO(mdan): the optimizer should be able to remove an invariant cond?
    extra_cond = (constant_op.constant(True),)  # dummy value, unused
    new_loop_vars = main_path()

scan_outputs = new_loop_vars, extra_cond
new_scan_state = new_loop_vars
exit((new_scan_state, scan_outputs))
