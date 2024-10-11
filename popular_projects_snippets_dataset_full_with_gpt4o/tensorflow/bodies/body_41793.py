# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Creates the attribute value corresponding to attribute_lib.IMPLEMENTS."""
attributes = {}
if isinstance(implements_arg, str):
    # First check if the attribute_lib.IMPLEMENTS is specified as a
    # NameAttrList. This is used when apart from the function name being
    # implemented, a list of attributes is also being specified.
    # The attributes are specified as key-value pairs in the NameAttrList
    # of the corresponding AttrValue. The function name will be in the
    # 'name' field of the NameAttrList. Else, it is just a string
    # corresponding to the function name.
    try:
        attr_value = attr_value_pb2.AttrValue()
        nameattrlist = attr_value_pb2.NameAttrList()
        _text_format.Merge(implements_arg, nameattrlist)
        attr_value.func.CopyFrom(nameattrlist)
        attributes[attributes_lib.IMPLEMENTS] = attr_value
    except (_text_format.ParseError, DecodeError):
        attributes[attributes_lib.IMPLEMENTS] = implements_arg
exit(attributes)
