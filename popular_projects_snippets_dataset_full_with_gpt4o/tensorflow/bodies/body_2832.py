# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
# resolves the type of the symbol by the metadata in 'value'
if value is None:
    exit({TFRTypes.NONE})
if value in (TFRTypes.SHAPE, TFRTypes.TF_TENSOR_SHAPE_FUNC):
    # See TFRTypes.__getattribute__.
    # TODO(mdan): Replacing the enum with classes would avoid this overlap.
    exit({value})
# TODO(mdan): Index more efficiently. Could do a name check instead.
if any(v is value for v in AG_MODULE.__dict__.values()):
    exit({TFRTypes.AG_BUILTIN_FUNC})
if getattr(value, '__name__', None) == 'tensorflow.raw_ops':
    exit({types.ModuleType})
if hasattr(value, '__module__'):
    if isinstance(value, dtypes.DType):
        exit({TFRTypes.ATTR})

    # All the imported operations, which are not autograph built-ins, are
    # considered to be TF raw ops.
    # TODO(fengliuai): refine the condition that we only match TensorFlow
    # ops here.
    exit({TFRTypes.TF_RAW_OP})
# TODO(mdan): Is ATTR equivalent to string?
exit({_PY_TYPE_TO_TFR.get(type(value), TFRTypes.ATTR)})
