# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
tester.assertEqual(set(dict_tensors.keys()), set(expected_tensors.keys()))

i = 0  # Index into the flattened output of session.run()
for k, v in dict_tensors.items():
    expected_v = expected_tensors[k]
    tf_logging.info("Comparing key: %s", k)
    if isinstance(v, sparse_tensor.SparseTensor):
        # Three outputs for SparseTensor : indices, values, shape.
        tester.assertEqual([k, len(expected_v)], [k, 3])
        tester.assertAllEqual(expected_v[0], flat_output[i])
        tester.assertAllEqual(expected_v[1], flat_output[i + 1])
        tester.assertAllEqual(expected_v[2], flat_output[i + 2])
        i += 3
    else:
        # One output for standard Tensor.
        tester.assertAllEqual(expected_v, flat_output[i])
        i += 1
