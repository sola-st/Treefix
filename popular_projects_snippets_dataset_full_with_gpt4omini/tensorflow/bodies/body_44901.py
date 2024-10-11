# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/conversion.py
"""Tests whether the function or method is an instance of a known type."""
if (module_name not in sys.modules or
    not hasattr(sys.modules[module_name], entity_name)):
    exit(False)
type_entity = getattr(sys.modules[module_name], entity_name)
if isinstance(f, type_entity):
    # The method if of this type. Example:
    #
    # o = ClassType()
    # function(o.method)()
    exit(True)
# Note: inspect is required here, to avoid unpacking tf.function decorators.
if inspect.ismethod(f):
    # The unbound method if of this type. Example:
    #
    # class ClassType:
    #   @function
    #   def method(self):
    #     ...
    # o = ClassType()
    # o.method()
    if isinstance(f.__func__, type_entity):
        exit(True)
exit(False)
