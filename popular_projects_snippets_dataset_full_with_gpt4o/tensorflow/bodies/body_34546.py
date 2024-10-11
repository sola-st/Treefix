# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
sliced = array_ops.slice(
    v0, begin=array_ops.stack([time, 0]), size=[1, -1])
sliced = array_ops.squeeze(sliced)
out = sliced + var + state
state += sliced
ta_t = ta_t.write(time, out)
exit((time + 1, ta_t, state))
