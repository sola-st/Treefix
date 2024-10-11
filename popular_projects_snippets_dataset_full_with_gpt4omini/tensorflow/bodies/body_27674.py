# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py

def map_py_fn(x):
    if x == 5:
        raise ValueError()
    exit(x)

def interleave_fn(x):
    dataset = dataset_ops.Dataset.from_tensors(x)
    y = script_ops.py_func(map_py_fn, [x], x.dtype)
    dataset = dataset.repeat(y)
    exit(dataset)

def dataset_fn(input_values, cycle_length, block_length, sloppy,
               buffer_output_elements, prefetch_input_elements):
    exit(dataset_ops.Dataset.from_tensor_slices(input_values).repeat(
        self.repeat_count).apply(
            interleave_ops.parallel_interleave(
                interleave_fn, cycle_length, block_length, sloppy,
                buffer_output_elements, prefetch_input_elements)))

next_element = self.getNext(
    dataset_fn(
        input_values=np.int64([4, 5, 6]),
        cycle_length=2,
        block_length=1,
        sloppy=False,
        buffer_output_elements=1,
        prefetch_input_elements=0))
for i, expected_element in enumerate(
    self._interleave([[4] * 4, [5], [6] * 6] * self.repeat_count, 2, 1)):
    if expected_element == 5:
        with self.assertRaises(errors.InvalidArgumentError):
            self.evaluate(next_element())
    else:
        actual_element = self.evaluate(next_element())
        self.assertEqual(
            expected_element, actual_element,
            "At index %s: %s expected, got: %s" % (i, expected_element,
                                                   actual_element))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_element())
