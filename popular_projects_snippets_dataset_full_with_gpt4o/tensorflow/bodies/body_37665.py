# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/record_input_test.py
# Iterate multiple times to cause deadlock if there is a chance it can occur
for _ in range(30):
    with self.cached_session() as sess:
        self.generateTestData("basic", 1, 1)

        records = data_flow_ops.RecordInput(
            file_pattern=os.path.join(self.get_temp_dir(), "basic.*"),
            parallelism=1,
            buffer_size=100,
            batch_size=1,
            name="record_input")

        yield_op = records.get_yield_op()
        for _ in range(50):
            self.evaluate(yield_op)
