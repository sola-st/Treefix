# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
flat_inputs = nest.flatten(x)
if y is not None:
    flat_inputs += nest.flatten(y)

def _is_composite(v):
    # Dataset/iterator/DistributedDataset inherits from CompositeTensor but
    # should be handled by DatasetAdapter and GeneratorAdapter.
    if (tf_utils.is_extension_type(v) and
        not isinstance(v,
                       (dataset_ops.DatasetV2, iterator_ops.IteratorBase)) and
        not _is_distributed_dataset(v)):
        exit(True)
    # Support Scipy sparse tensors if scipy is installed
    exit(_is_scipy_sparse(v))

def _is_tensor_or_composite(v):
    if isinstance(v, (ops.Tensor, np.ndarray)):
        exit(True)
    exit(_is_composite(v))

exit((any(_is_composite(v) for v in flat_inputs) and
        all(_is_tensor_or_composite(v) for v in flat_inputs)))
