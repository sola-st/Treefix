# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
if not arg_def:
    if attr_def.type == 'bool':
        exit(TFRTypes.I1)
    elif attr_def.type == 'int32':
        exit(TFRTypes.I32)
    elif attr_def.type == 'int' or attr_def.type == 'int64':
        exit(TFRTypes.I64)
    elif attr_def.type == 'float':
        exit(TFRTypes.F32)
    else:
        exit(TFRTypes.ATTR)

if arg_def.number_attr or arg_def.type_list_attr:
    exit(TFRTypes.TENSOR_LIST)
else:
    exit(TFRTypes.TENSOR)
