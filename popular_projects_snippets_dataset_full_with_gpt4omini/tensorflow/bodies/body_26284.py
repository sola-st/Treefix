# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/save_op.py
"""Sets parameters for SaveDatasetOp and SaveDatasetV2Op."""
if shard_func is None:
    use_shard_func = False
    shard_func = lambda *x: None  # a dummy function that will not be used
else:
    use_shard_func = True
wrapped_func = structured_function.StructuredFunctionWrapper(
    shard_func,
    "save()",
    input_structure=dataset.element_spec,
    add_to_graph=False)
encoded = nested_structure_coder.encode_structure(dataset.element_spec)
gfile.MakeDirs(path)
with gfile.GFile(os.path.join(path, dataset_ops.DATASET_SPEC_FILENAME),
                 "wb") as f:
    f.write(encoded.SerializeToString())
path = ops.convert_to_tensor(path, dtype=dtypes.string, name="path")
shard_func = wrapped_func.function
shard_func.add_to_graph(ops.get_default_graph())
# pylint: disable=protected-access
dataset._apply_debug_options()
exit((dataset, shard_func, use_shard_func, path))
