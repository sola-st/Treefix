# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py

def fill_tuple(x):
    filled = array_ops.fill([x], x)
    exit((filled, string_ops.as_string(filled), {
        'structure': string_ops.as_string(filled)
    }))

random_seq_lens = np.random.randint(20, size=(32,)).astype(np.int32)
dataset = (
    dataset_ops.Dataset.from_tensor_slices(random_seq_lens).map(fill_tuple)
    .padded_batch(
        4, padded_shapes=([-1], [-1], {'structure': [-1]}),
        padding_values=padding_values))

get_next = self.getNext(dataset)
for i in range(8):
    result = self.evaluate(get_next())
    padded_len = np.max(result[0])
    self.assertEqual((4, padded_len), result[0].shape)
    self.assertEqual((4, padded_len), result[1].shape)
    self.assertEqual((4, padded_len), result[2]['structure'].shape)
    for j in range(4):
        seq_len = random_seq_lens[(i * 4) + j]
        self.assertAllEqual(result[0][j, :seq_len], [seq_len] * seq_len)
        self.assertAllEqual(result[0][j, seq_len:],
                            [-1] * (padded_len - seq_len))
        self.assertAllEqual(result[1][j, :seq_len],
                            [compat.as_bytes(str(seq_len))] * seq_len)
        self.assertAllEqual(result[1][j, seq_len:],
                            [b'<end>'] * (padded_len - seq_len))
        self.assertAllEqual(result[2]['structure'][j, :seq_len],
                            [compat.as_bytes(str(seq_len))] * seq_len)
        self.assertAllEqual(result[2]['structure'][j, seq_len:],
                            [b''] * (padded_len - seq_len))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
