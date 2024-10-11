# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
all_elt_types = set()
for t in elt_types:
    all_elt_types |= t

if len(all_elt_types) != 1:
    all_elt_types = self._coerce_to_more_specific_type(all_elt_types)

if len(all_elt_types) != 1:
    raise ValueError('ambiguous list element types: {}'.format(elt_types))

if TFRTypes.TENSOR in all_elt_types:
    exit({TFRTypes.TENSOR_LIST})
exit({TFRTypes.ATTR})
