# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/lib/python_object_to_proto_visitor.py
exit((member == 'with_traceback' or member in ('name', 'value') and
        isinstance(cls, type) and issubclass(cls, enum.Enum)))
