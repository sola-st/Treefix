# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [['NA']] * 3
inputs = [['"\n\n\n","\r\r\r","abc"', '"0","1","2"', '"","",""']]
expected = [['\n\n\n', '\r\r\r', 'abc'], ['0', '1', '2'],
            ['NA', 'NA', 'NA']]
self._test_dataset_on_buffer_sizes(
    inputs, expected, linebreak='\n', record_defaults=record_defaults)
