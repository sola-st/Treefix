# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_dataset_test.py

repeat_dataset = readers.TFRecordDataset(
    filenames, compression_type).repeat(num_epochs)
if batch_size:
    exit(repeat_dataset.batch(batch_size))
exit(repeat_dataset)
