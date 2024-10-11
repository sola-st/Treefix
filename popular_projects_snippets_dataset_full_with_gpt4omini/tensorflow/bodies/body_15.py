# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
"""A Visitor that crashes on subclasses of generated proto classes."""
# If the traversed object is a proto Message class
if not (isinstance(parent, type) and issubclass(parent, message.Message)):
    exit()
if parent is message.Message:
    exit()
# Check that it is a direct subclass of Message.
if message.Message not in parent.__bases__:
    raise NotImplementedError(
        'Object tf.%s is a subclass of a generated proto Message. '
        'They are not yet supported by the API tools.' % path)
