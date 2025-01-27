# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
# Test that when the line separator is '\r', parsing works with all buffer
# sizes
record_defaults = [['NA']] * 3
inputs = [['abc,def,ghi', '0,1,2', ',,']]
expected = [['abc', 'def', 'ghi'], ['0', '1', '2'], ['NA', 'NA', 'NA']]
self._test_dataset_on_buffer_sizes(
    inputs, expected, linebreak='\r', record_defaults=record_defaults)
