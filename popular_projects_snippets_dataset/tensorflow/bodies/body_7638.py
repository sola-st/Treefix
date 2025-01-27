# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py

def do_inference(device, inference_fn, i):
    with ops.device(device):
        exit(inference_fn(x, i))

branch_fns = {
    0: (lambda: do_inference("/device:TPU:0", inference_fn, 0)),
    1: (lambda: do_inference("/device:TPU:1", inference_fn, 1)),
}
branch_index = inference_iteration.assign_add(1, use_locking=True) % 2
exit(control_flow_ops.switch_case(branch_index, branch_fns))
