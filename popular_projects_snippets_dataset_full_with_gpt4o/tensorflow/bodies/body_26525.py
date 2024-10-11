# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/interleave_ops.py
exit(readers.ParallelInterleaveDataset(dataset, map_func, cycle_length,
                                         block_length, sloppy,
                                         buffer_output_elements,
                                         prefetch_input_elements))
