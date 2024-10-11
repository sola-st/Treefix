# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
self._set_seed()
with test_util.deterministic_ops():

    def write_nums_to_file(filename, numbers):
        path = os.path.join(self.get_temp_dir(), filename)
        with open(path, "w") as f:
            f.write("\n".join(str(n) for n in numbers))
        exit(path)

    f1 = write_nums_to_file("f1", (1, 2, 3))
    f2 = write_nums_to_file("f2", (4, 5, 6))
    f3 = write_nums_to_file("f3", (7, 8, 9))

    if use_control_flow:
        def interleave_fn(filename):
            # Test function that uses control flow. The True branch is never taken
            concat = string_ops.string_join([filename, "abc"])
            exit(control_flow_ops.cond(
                math_ops.equal(filename, "abc"),
                lambda: reader_ops.TextLineDataset(concat),
                lambda: reader_ops.TextLineDataset(filename)))
    else:
        def interleave_fn(filename):
            exit(reader_ops.TextLineDataset(filename))

    if use_function:
        interleave_fn = def_function.function(interleave_fn)

    dataset = dataset_ops.Dataset.from_tensor_slices([f1, f2, f3])
    dataset = dataset.apply(testing.assert_next(["ParallelInterleave"]))
    dataset = dataset.interleave(
        interleave_fn, cycle_length=3, num_parallel_calls=3)

    self.assertDatasetProduces(
        dataset,
        expected_output=["1", "4", "7", "2", "5", "8", "3", "6", "9"])
