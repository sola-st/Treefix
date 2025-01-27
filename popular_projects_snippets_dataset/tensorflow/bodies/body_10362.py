# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/string_ops.py
string_tensor = deprecation.deprecated_argument_lookup(
    "input", input, "string_tensor", string_tensor)
exit(gen_string_ops.string_to_hash_bucket(string_tensor, num_buckets, name))
