# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
num_files = 5
lines_per_file = 5
num_outputs = num_files * lines_per_file
test_filenames = self._createFiles(
    num_files, lines_per_file, crlf=True, compression_type=compression_type)
verify_fn(
    self,
    lambda: self._build_iterator_graph(test_filenames, compression_type),
    num_outputs)
