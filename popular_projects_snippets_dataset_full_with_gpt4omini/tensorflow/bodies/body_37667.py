# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/record_input_test.py
files = 10
records_per_file = 10
batches = 2
with self.cached_session() as sess:
    self.generateTestData("basic", files, records_per_file)

    records = data_flow_ops.RecordInput(
        file_pattern=os.path.join(self.get_temp_dir(), "basic.*"),
        parallelism=2,
        buffer_size=2000,
        batch_size=1,
        shift_ratio=0.33,
        seed=10,
        name="record_input",
        batches=batches)

    yield_op = records.get_yield_op()

    # cycle over 3 epochs and make sure we never duplicate
    for _ in range(3):
        epoch_set = set()
        for _ in range(int(files * records_per_file / batches)):
            op_list = self.evaluate(yield_op)
            self.assertTrue(len(op_list) is batches)
            for r in op_list:
                self.assertTrue(r[0] not in epoch_set)
                epoch_set.add(r[0])
