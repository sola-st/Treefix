# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
seq_lens = np.random.randint(20, size=(count,)).astype(np.int32)
batch_size = 4
dataset = dataset_ops.Dataset.from_tensor_slices(seq_lens).map(
    lambda x: array_ops.fill([x], x)).padded_batch(
        batch_size=batch_size,
        drop_remainder=drop_remainder,
        padded_shapes=padded_shapes)

num_full_batches = len(seq_lens) // batch_size
get_next = self.getNext(dataset)
for i in range(num_full_batches):
    result = self.evaluate(get_next())
    padded_len = padded_shapes[0]
    if padded_len is None or padded_len == -1:
        padded_len = np.max(result) if result.size > 0 else 0
    self.assertEqual((batch_size, padded_len), result.shape)
    for j in range(batch_size):
        seq_len = seq_lens[(i * batch_size) + j]
        self.assertAllEqual(result[j, :seq_len], [seq_len] * seq_len)
        self.assertAllEqual(result[j, seq_len:], [0] * (padded_len - seq_len))

if not drop_remainder and len(seq_lens) % batch_size > 0:
    result = self.evaluate(get_next())
    padded_len = padded_shapes[0]
    if padded_len is None or padded_len == -1:
        padded_len = np.max(result) if result.size > 0 else 0
    self.assertEqual((len(seq_lens) % batch_size, padded_len), result.shape)
    for j in range(len(seq_lens) % batch_size):
        seq_len = seq_lens[num_full_batches * batch_size + j]
        self.assertAllEqual(result[j, :seq_len], [seq_len] * seq_len)
        self.assertAllEqual(result[j, seq_len:], [0] * (padded_len - seq_len))

with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
