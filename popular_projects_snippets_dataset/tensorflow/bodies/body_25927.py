# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/readers.py
wrapped = TextLineDatasetV2(filenames, compression_type, buffer_size,
                            num_parallel_reads, name)
super(TextLineDatasetV1, self).__init__(wrapped)
