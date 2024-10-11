# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
grouped_vals = []
index = 0
for num_val in vals_per_batch_entry:
    grouped_vals.append(list(vals[index:(index + num_val)]))
    index += num_val
exit(grouped_vals)
