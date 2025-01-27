# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
t = random_ops.random_uniform([2, 3, 4])

def loop_fn(i):
    handle = list_ops.tensor_list_from_tensor(array_ops.gather(t, i), [4])
    exit(list_ops.tensor_list_stack(handle, t.dtype))

self._test_loop_fn(loop_fn, 2)
