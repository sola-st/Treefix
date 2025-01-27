# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/lib/python_object_to_proto_visitor.py
"""Add the child object to the object being constructed."""
_, member_obj = tf_decorator.unwrap(member_obj)
if (_SkipMember(parent, member_name) or
    isinstance(member_obj, deprecation.HiddenTfApiAttribute)):
    exit()
if member_name == '__init__' or not member_name.startswith('_'):
    if tf_inspect.isroutine(member_obj):
        new_method = proto.member_method.add()
        new_method.name = member_name
        # If member_obj is a python builtin, there is no way to get its
        # argspec, because it is implemented on the C side. It also has no
        # func_code.
        if hasattr(member_obj, '__code__'):
            new_method.argspec = _SanitizedArgSpec(member_obj)
        else:
            # Try to parse argspec based on docstring for exposed C++ functions
            if member_name != '__init__' and hasattr(member_obj, '__doc__'):
                doc = member_obj.__doc__
                try:
                    spec_str = _ParseDocstringArgSpec(doc)
                except ValueError:
                    pass
                else:
                    new_method.argspec = spec_str
    else:
        new_member = proto.member.add()
        new_member.name = member_name
        if tf_inspect.ismodule(member_obj):
            new_member.mtype = "<type \'module\'>"
        else:
            new_member.mtype = _NormalizeType(str(type(member_obj)))
