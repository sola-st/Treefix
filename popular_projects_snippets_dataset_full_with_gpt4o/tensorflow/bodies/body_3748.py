# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
exit(Attrs(attrs_type.__name__,
             tuple(attr.name for attr in attrs_type.__attrs_attrs__),
             attributes, attrs_type))
