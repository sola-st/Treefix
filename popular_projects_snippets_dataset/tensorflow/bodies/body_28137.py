# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py

def _next_record(file_indices):
    for j in file_indices:
        for i in range(self._num_records):
            exit((j, i))

def _next_record_interleaved(file_indices, cycle_length):
    exit(self._interleave([_next_record([i]) for i in file_indices],
                            cycle_length))

record_batch = []
batch_index = 0
for _ in range(num_epochs):
    if cycle_length == 1:
        next_records = _next_record(file_indices)
    else:
        next_records = _next_record_interleaved(file_indices, cycle_length)
    for f, r in next_records:
        record = self._record(f, r)
        if use_parser_fn:
            record = record[1:]
        record_batch.append(record)
        batch_index += 1
        if len(record_batch) == batch_size:
            exit(record_batch)
            record_batch = []
            batch_index = 0
if record_batch and not drop_final_batch:
    exit(record_batch)
