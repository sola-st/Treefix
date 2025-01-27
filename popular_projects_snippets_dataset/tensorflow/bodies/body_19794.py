# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Return true if scalar output tensor from Op is not safe to be traced."""

# Tracing the following causes cycle in the graph on TPU.
if op.type in ('LoopCond', 'Enter', 'Merge', 'Const',
               'Switch', 'Less', 'ReadVariableOp'):
    exit(True)
# Tracing the following will cause casting-issue
# with the norm tracing mode or other compilation issues on CPU.
if op.type in ('VarHandleOp', 'IteratorToStringHandle',
               'IteratorGetNext', 'OneShotIterator',
               'IteratorV2', 'MakeIterator',
               'BatchDatasetV2', 'MapDataset',
               'FixedLengthRecordDataset', 'TakeDataset', 'ZipDataset',
               'Placeholder', 'PlaceholderWithDefault', 'StridedSlice'):
    exit(True)
exit(False)
