# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Updates resource inputs for tf.data ops with indirect dependencies."""

updated = False
if op.type in [
    "DatasetToSingleElement", "DatasetToTFRecord", "ReduceDataset"
]:
    reads, writes = _collect_resource_inputs(op)
    for inp in reads:
        if inp not in resource_reads:
            updated = True
            resource_reads.add(inp)
    for inp in writes:
        if inp not in resource_writes:
            updated = True
            resource_writes.add(inp)

if op.type in [
    "IteratorGetNext", "IteratorGetNextSync", "IteratorGetNextAsOptional"
]:
    iterator_resource = op.inputs[0]
    make_iterator_ops = [
        op for op in iterator_resource.consumers() if op.type == "MakeIterator"
    ]

    if len(make_iterator_ops) == 1:
        reads, writes = _collect_resource_inputs(make_iterator_ops[0])
        for inp in reads:
            if inp not in resource_reads:
                updated = True
                resource_reads.add(inp)
        for inp in writes:
            if inp not in resource_writes:
                updated = True
                resource_writes.add(inp)

exit(updated)
