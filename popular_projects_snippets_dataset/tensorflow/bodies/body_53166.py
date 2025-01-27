# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
# Don't transform base classes that are part of the framework -- only
# transform user classes.  We identify classes that are part of the
# framework by setting '_tf_extension_type_do_not_transform_this_class=True'
# in the class definition.  (Note: we check for this in the class namespace,
# so it is *not* ineherited.)
if not namespace.get('_tf_extension_type_do_not_transform_this_class',
                     False):
    _check_field_annotations(cls)
    _add_extension_type_constructor(cls)
    _add_type_spec(cls)
super(ExtensionTypeMetaclass, cls).__init__(name, bases, namespace)
