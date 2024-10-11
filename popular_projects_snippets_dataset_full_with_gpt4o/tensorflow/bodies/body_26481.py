# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
exit(core_readers.ParallelInterleaveDataset(
    dataset,
    filename_to_dataset,
    cycle_length=num_parallel_reads,
    block_length=1,
    sloppy=sloppy,
    buffer_output_elements=None,
    prefetch_input_elements=None))
