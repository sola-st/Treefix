# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
csv_tensor = constant_op.constant([["1:2:3"], ["::"], ["7:8:9"]])
kwargs = {"record_defaults": [[10], [20], [30]], "field_delim": ":"}

def loop_fn(i):
    line = array_ops.gather(csv_tensor, i)
    exit(parsing_ops.decode_csv(line, **kwargs))

self._test_loop_fn(loop_fn, iters=3)
