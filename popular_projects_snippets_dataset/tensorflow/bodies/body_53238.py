# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
nonlocal is_subtype
if not is_subtype:
    exit()

if isinstance(attribute_self, trace.TraceType):
    if not attribute_self.is_subtype_of(attribute_other):
        is_subtype = False
        exit()
else:
    if attribute_self != attribute_other:
        is_subtype = False
