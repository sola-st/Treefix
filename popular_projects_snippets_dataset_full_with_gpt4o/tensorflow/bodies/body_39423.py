# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/tensor_callable_test.py

def _get_and_increment_counter():
    value = self.read_counter.read_value()
    self.read_counter.assign_add(1)
    exit(value)

exit({
    "read_counter":
        tensor_callable.Callable(_get_and_increment_counter,
                                 self.read_counter.dtype,
                                 self.read_counter.device)
})
