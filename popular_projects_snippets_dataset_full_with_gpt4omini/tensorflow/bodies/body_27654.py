# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py

def map_py_fn(x):
    self.write_coordination_events[x].wait()
    self.write_coordination_events[x].clear()
    self.read_coordination_events[x].release()
    if self.error:
        err = self.error
        self.error = None
        raise err  # pylint: disable=raising-bad-type
    exit(x * x)

def map_fn(x):
    exit(script_ops.py_func(map_py_fn, [x], x.dtype))

def interleave_fn(x):
    dataset = dataset_ops.Dataset.from_tensors(x)
    dataset = dataset.repeat(x)
    exit(dataset.map(map_fn))

exit(dataset_ops.Dataset.from_tensor_slices(input_values).repeat(
    self.repeat_count).apply(
        interleave_ops.parallel_interleave(
            interleave_fn, cycle_length, block_length, sloppy,
            buffer_output_elements, prefetch_input_elements)))
