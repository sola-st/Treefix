# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
# In this case, we expect it to behave differently from
# TextLineDataset->map(decode_csv) since that flow has bugs
record_defaults = [['']] * 4
inputs = [['a,b,"""c""\n0","d\ne"', 'f,g,h,i']]
expected = [['a', 'b', '"c"\n0', 'd\ne'], ['f', 'g', 'h', 'i']]
self._test_dataset(inputs, expected, record_defaults=record_defaults)
