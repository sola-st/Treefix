# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops_test.py
# Example of typical preprocessing of string to numeric feature
hashed = string_to_hash_bucket(elem['str'], 10)
# For dense string case, slice it to size of ragged int
hashed_sliced = hashed[:, :elem['size'][0]]
# Computation with both feature from string and numeric dataset output
exit(reduce_sum(hashed_sliced) + 100 * reduce_sum(elem['int']))
