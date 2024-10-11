# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/padded_batch_op.py
if not isinstance(component_spec, tensor_spec.TensorSpec):
    if isinstance(component_spec, dataset_ops.DatasetSpec):
        raise TypeError(
            "`padded_batch` is not supported for datasets of datasets")
    raise TypeError(f"`padded_batch` is only supported for datasets that "
                    f"produce tensor elements but type spec of elements in "
                    f"the input dataset is not a subclass of TensorSpec: "
                    f"`{component_spec}`.")
