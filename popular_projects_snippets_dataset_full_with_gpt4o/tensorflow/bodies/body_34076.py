# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
indices_val, keys_val, values_val = sess.run(
    [take_t[0], take_t[1], take_t[2][0]])
self.assertAllEqual(indices_val,
                    [int(x.decode("ascii")) - 2**63 for x in keys_val])
self.assertItemsEqual(zip(keys, values), zip(keys_val, values_val))
