# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
indices_val, keys_val, values_0_val, values_1_val = sess.run([
    take_ops[i][0], take_ops[i][1], take_ops[i][2][0], take_ops[i][2][1]
])
taken.append({
    "indices": indices_val,
    "keys": keys_val,
    "values_0": values_0_val,
    "values_1": values_1_val
})
