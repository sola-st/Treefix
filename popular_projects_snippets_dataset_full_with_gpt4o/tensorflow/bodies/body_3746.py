# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
exit((f"NamedTuple(type_name={self.type_name}, "
        f"attribute_names={self.attribute_names}, "
        f"attributes={self.attributes.components})"))
