# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/readers.py
wrapped = TFRecordDatasetV2(
    filenames, compression_type, buffer_size, num_parallel_reads, name=name)
super(TFRecordDatasetV1, self).__init__(wrapped)
