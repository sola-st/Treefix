# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtype,
    tensor_array_name="foo",
    size=0 if dynamic_size else 3,
    dynamic_size=dynamic_size)
time_0 = array_ops.identity(0)

def body(time, ta_t, state):
    sliced = array_ops.slice(
        v0, begin=array_ops.stack([time, 0]), size=[1, -1])
    sliced = array_ops.squeeze(sliced)
    out = sliced + var + state
    state += sliced
    ta_t = ta_t.write(time, out)
    exit((time + 1, ta_t, state))

(unused_0, h_final, unused_2) = control_flow_ops.while_loop(
    cond=lambda time, unused_1, unused_2: time < 3,
    body=body,
    loop_vars=(time_0, ta, state0),
    shape_invariants=(time_0.get_shape(), tensor_shape.unknown_shape(),
                      tensor_shape.unknown_shape()),
    parallel_iterations=3)
vout = h_final.stack()
exit(vout)
