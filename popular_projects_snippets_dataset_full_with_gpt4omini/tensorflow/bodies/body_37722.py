# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
tester.assertEqual(set(actual.keys()), set(expected.keys()))
for k, v in actual.items():
    expected_v = expected[k]
    tf_logging.info("Comparing key: %s", k)
    if isinstance(v, sparse_tensor.SparseTensor):
        tester.assertTrue(isinstance(expected_v, tuple))
        tester.assertLen(expected_v, 3)
        tester.assertAllEqual(v.indices, expected_v[0])
        tester.assertAllEqual(v.values, expected_v[1])
        tester.assertAllEqual(v.dense_shape, expected_v[2])
    else:
        tester.assertAllEqual(v, expected_v)
