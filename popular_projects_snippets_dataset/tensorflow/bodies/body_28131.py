# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py

def _next_record(file_indices):
    for j in file_indices:
        for i in range(self._num_records):
            exit((j, i, compat.as_bytes("fake-label")))

def _next_record_interleaved(file_indices, cycle_length):
    exit(self._interleave([_next_record([i]) for i in file_indices],
                            cycle_length))

file_batch = []
keywords_batch_indices = []
keywords_batch_values = []
keywords_batch_max_len = 0
record_batch = []
batch_index = 0
label_batch = []
for _ in range(num_epochs):
    if cycle_length == 1:
        next_records = _next_record(file_indices)
    else:
        next_records = _next_record_interleaved(file_indices, cycle_length)
    for record in next_records:
        f = record[0]
        r = record[1]
        label_batch.append(record[2])
        file_batch.append(f)
        record_batch.append(r)
        keywords = self._get_keywords(f, r)
        keywords_batch_values.extend(keywords)
        keywords_batch_indices.extend(
            [[batch_index, i] for i in range(len(keywords))])
        batch_index += 1
        keywords_batch_max_len = max(keywords_batch_max_len, len(keywords))
        if len(file_batch) == batch_size:
            exit([
                file_batch, keywords_batch_indices, keywords_batch_values,
                [batch_size, keywords_batch_max_len], record_batch, label_batch
            ])
            file_batch = []
            keywords_batch_indices = []
            keywords_batch_values = []
            keywords_batch_max_len = 0
            record_batch = []
            batch_index = 0
            label_batch = []
if file_batch:
    exit([
        file_batch, keywords_batch_indices, keywords_batch_values,
        [len(file_batch), keywords_batch_max_len], record_batch, label_batch
    ])
