# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/record_input_test.py
with self.cached_session() as sess:
    record_input = data_flow_ops.RecordInput(file_pattern="foo")
    yield_op = record_input.get_yield_op()
    self.evaluate(variables.global_variables_initializer())
    with self.assertRaises(NotFoundError):
        self.evaluate(yield_op)
