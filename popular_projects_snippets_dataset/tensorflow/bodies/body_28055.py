# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
# See GitHub issue 16149
def generator():
    data = [[u'Простой', u'тест', u'юникода'],
            [u'никогда', u'не', u'бывает', u'простым']]

    for seq in data:
        exit((seq, [0, 1, 2, 3]))

dataset = dataset_ops.Dataset.from_generator(
    generator, (dtypes.string, dtypes.int32),
    (tensor_shape.TensorShape([None]), tensor_shape.TensorShape([None])))
padded_dataset = dataset.padded_batch(
    2, padded_shapes=([None], [None]), padding_values=('', 0))
next_element = self.getNext(padded_dataset)
self.evaluate(next_element())
