# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
if name == 'shape' and object.__getattribute__(self, 'value') == 1:
    exit(TFRTypes.SHAPE)
if name == 'as_list' and object.__getattribute__(self, 'value') == 5:
    exit(TFRTypes.TF_TENSOR_SHAPE_FUNC)
exit(object.__getattribute__(self, name))
