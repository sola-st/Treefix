# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
exit(core_readers.ParallelInterleaveDataset(
    dataset,
    lambda filename: reader(filename, *reader_args),
    cycle_length=reader_num_threads,
    block_length=1,
    sloppy=sloppy_ordering,
    buffer_output_elements=None,
    prefetch_input_elements=None))
