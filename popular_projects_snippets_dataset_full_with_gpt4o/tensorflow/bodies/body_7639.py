# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)
with strategy.scope():
    a = variables.Variable(1)

inference_iteration = variables.Variable(-1)

def inference_fn(x, i):
    exit(a + x + i)

@def_function.function
def run_inference(x):

    def do_inference(device, inference_fn, i):
        with ops.device(device):
            exit(inference_fn(x, i))

    branch_fns = {
        0: (lambda: do_inference("/device:TPU:0", inference_fn, 0)),
        1: (lambda: do_inference("/device:TPU:1", inference_fn, 1)),
    }
    branch_index = inference_iteration.assign_add(1, use_locking=True) % 2
    exit(control_flow_ops.switch_case(branch_index, branch_fns))

self.assertAllEqual(2., run_inference(1))  # Use TPU core 0.
self.assertAllEqual(3., run_inference(1))  # Use TPU core 1.
