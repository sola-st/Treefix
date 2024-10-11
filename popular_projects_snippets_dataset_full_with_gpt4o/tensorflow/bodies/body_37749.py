# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
# Test using tf.io.parse_single_sequence_example
self._test(
    kwargs,
    expected_context_values=expected_context_values,
    expected_feat_list_values=expected_feat_list_values,
    expected_err=expected_err,
    batch=False)

# Convert the input to a batch of size 1, and test using
# tf.parse_sequence_example.

# Some replacements are needed for the batch version.
kwargs["serialized"] = [kwargs.pop("serialized")]
kwargs["example_names"] = [kwargs.pop("example_name")
                          ] if "example_name" in kwargs else None

# Add a batch dimension to expected output
if expected_context_values:
    new_values = {}
    for k in expected_context_values:
        v = expected_context_values[k]
        if isinstance(kwargs["context_features"][k],
                      (parsing_ops.FixedLenFeature, parsing_ops.RaggedFeature)):
            new_values[k] = np.expand_dims(v, axis=0)
        else:
            # Sparse tensor.
            new_values[k] = (np.insert(v[0], 0, 0,
                                       axis=1), v[1], np.insert(v[2], 0, 1))
    expected_context_values = new_values

expected_length_values = {}
if expected_feat_list_values:
    new_values = {}
    for k in expected_feat_list_values:
        v = expected_feat_list_values[k]
        if isinstance(kwargs["sequence_features"][k],
                      parsing_ops.FixedLenSequenceFeature):
            expected_length_values[k] = [np.shape(v)[0]]
            new_values[k] = np.expand_dims(v, axis=0)
        elif isinstance(kwargs["sequence_features"][k],
                        parsing_ops.RaggedFeature):
            new_values[k] = np.expand_dims(v, axis=0)
        else:
            # Sparse tensor.
            new_values[k] = (np.insert(v[0], 0, 0,
                                       axis=1), v[1], np.insert(v[2], 0, 1))
    expected_feat_list_values = new_values

self._test(
    kwargs,
    expected_context_values=expected_context_values,
    expected_feat_list_values=expected_feat_list_values,
    expected_length_values=expected_length_values,
    expected_err=expected_err,
    batch=True)
