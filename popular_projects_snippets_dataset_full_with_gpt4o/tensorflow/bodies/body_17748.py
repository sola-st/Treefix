# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
exit((isinstance(value, composite_tensor.CompositeTensor)
        # Leave sparse tensors to be converted by `PFor._convert_sparse`.
        and not isinstance(value, sparse_tensor.SparseTensor)
        and not isinstance(value, indexed_slices.IndexedSlices)))
