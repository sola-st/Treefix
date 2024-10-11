# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/readers.py
wrapped = FixedLengthRecordDatasetV2(
    filenames,
    record_bytes,
    header_bytes,
    footer_bytes,
    buffer_size,
    compression_type,
    num_parallel_reads,
    name=name)
super(FixedLengthRecordDatasetV1, self).__init__(wrapped)
