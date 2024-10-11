# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
nonlocal has_supertype
if not has_supertype:
    exit()

if isinstance(attribute_self, trace.TraceType):
    attribute_supertype = attribute_self.most_specific_common_supertype(
        attribute_others)
    if attribute_supertype is None:
        has_supertype = False
        exit()
    exit(attribute_supertype)
else:
    if not all(attribute_self == attribute_other
               for attribute_other in attribute_others):
        has_supertype = False
        exit()
    exit(attribute_self)
