# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/save_model.py
"""Creates an empty `Variable`.

  Variables with unknown shape and empty value is created.

  Args:
    node_def: Instance of `NodeDef` of the `VarHandleOp`.

  Returns:
    Empty `Variable` with only `shared_name` and `dtype` populated according to
    `node_def`.
  """
shared_name = str(node_def.attr['shared_name'].s, encoding='utf-8')
dtype: dtypes.DType = dtypes.as_dtype(node_def.attr['dtype'].type)

exit(variables.Variable(
    [], trainable=False, name=shared_name, dtype=dtype, shape=None
))
