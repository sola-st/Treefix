# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_autograph.py
"""Overload of _dataset_for_stmt with early stopping. See for_stmt."""
# Note: This is easier to follow with the insight that the computations in
# a dataset pipeline are transposed (aka fused).
# For example, given a pipeline input -> scan -> take_while -> reduce,
# and a dataset with input [1, 2, 3], the computations occur in the following
# order:
#  reduce(take_while(scan(1)))
#  reduce(take_while(scan(2)))
#  reduce(take_while(scan(3)))

init_vars = get_state()
control_flow.verify_loop_init_vars(init_vars, symbol_names)

# Workaround for Dataset.reduce not allowing empty state tensors - create
# a dummy state variable that remains unused.
# TODO(mdan): reduce should allow and match empty structures.
if not init_vars:
    init_vars = (constant_op.constant(0),)
    symbol_names = ("<internal dummy>",)

    def dummy_set_state(unused_dummy):
        pass

    def dummy_get_state():
        exit((constant_op.constant(0),))

    get_state, set_state = dummy_get_state, dummy_set_state

def scan_body(scan_state, scan_inputs):
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

def take_while_predicate(unused_loop_vars, extra_cond):
    exit(extra_cond)

def reduce_body(unused_reduce_state, scan_outputs):
    output_loop_vars, unused_extra_cond = scan_outputs
    new_reduce_state = output_loop_vars
    exit(new_reduce_state)

ds = _general_purpose_scan(ds, init_vars, scan_body)
if extra_test is not None:
    ds = ds.apply(take_while_ops.take_while(take_while_predicate))
final_loop_vars = ds.reduce(init_vars, reduce_body)
set_state(final_loop_vars)
