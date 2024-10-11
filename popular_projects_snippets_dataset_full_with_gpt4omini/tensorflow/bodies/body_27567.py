# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py

if expected_err:
    with self.assertRaisesWithPredicateMatch(expected_err[0],
                                             expected_err[1]):
        dataset = dataset_ops.Dataset.from_tensors(input_tensor).apply(
            contrib_parsing_ops.parse_example_dataset(feature_val))
        get_next = self.getNext(dataset)
        self.evaluate(get_next())
    exit()
else:
    # Returns dict w/ Tensors and SparseTensors.
    # Check values.
    dataset = dataset_ops.Dataset.from_tensors(input_tensor).apply(
        contrib_parsing_ops.parse_example_dataset(feature_val))
    get_next = self.getNext(dataset)
    result = self.evaluate(get_next())
    self._compare_output_to_expected(result, expected_values)
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(get_next())
    with self.assertRaises(errors_impl.OutOfRangeError):
        self.evaluate(get_next())
    if create_iterator_twice:
        get_next = self.getNext(dataset)
        result = self.evaluate(get_next())
        self._compare_output_to_expected(result, expected_values)
        with self.assertRaises(errors_impl.OutOfRangeError):
            self.evaluate(get_next())
    # Check shapes; if serialized is a Tensor we need its size to
    # properly check.
batch_size = (
    self.evaluate(input_tensor).size if isinstance(input_tensor, ops.Tensor)
    else np.asarray(input_tensor).size)
for k, f in feature_val.items():
    if isinstance(f, parsing_ops.FixedLenFeature) and f.shape is not None:
        self.assertEqual(
            dataset_ops.get_legacy_output_shapes(dataset)[k].as_list()[0],
            batch_size)
    elif isinstance(f, parsing_ops.VarLenFeature):
        self.assertEqual(
            dataset_ops.get_legacy_output_shapes(dataset)[k].as_list()[1], None)
