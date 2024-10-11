# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/padded_batch_test.py
data = [[u'Простой', u'тест', u'юникода'],
        [u'никогда', u'не', u'бывает', u'простым']]

for seq in data:
    exit((seq, [0, 1, 2, 3]))
