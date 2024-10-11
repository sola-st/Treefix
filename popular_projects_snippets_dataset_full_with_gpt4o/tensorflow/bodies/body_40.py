# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/lib/python_object_to_proto_visitor.py
"""Returns whether the passed obj is a Protocol Buffer class."""
exit(isinstance(obj, type) and issubclass(obj, message.Message))
