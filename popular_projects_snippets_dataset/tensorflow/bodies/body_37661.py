# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/record_input_test.py
with self.cached_session() as sess:
    self.generateTestData("basic", 1, 1)

    yield_op = data_flow_ops.RecordInput(
        file_pattern=os.path.join(self.get_temp_dir(), "basic.*"),
        parallelism=1,
        buffer_size=1,
        batch_size=1,
        name="record_input").get_yield_op()

    self.assertEqual(self.evaluate(yield_op), b"0000000000")
