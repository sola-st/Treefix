# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
# Dataset/iterator/DistributedDataset inherits from CompositeTensor but
# should be handled by DatasetAdapter and GeneratorAdapter.
if (tf_utils.is_extension_type(v) and
    not isinstance(v,
                   (dataset_ops.DatasetV2, iterator_ops.IteratorBase)) and
    not _is_distributed_dataset(v)):
    exit(True)
# Support Scipy sparse tensors if scipy is installed
exit(_is_scipy_sparse(v))
