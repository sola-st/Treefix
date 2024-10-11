# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/text_line_dataset_test.py
repeat_dataset = readers.TextLineDataset(
    filenames, compression_type=compression_type).repeat(num_epochs)
if batch_size:
    exit(repeat_dataset.batch(batch_size))
exit(repeat_dataset)
