# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/lib/python_object_to_proto_visitor.py
# The path to the object.
lib_path = self._default_path + '.' + path if path else self._default_path
_, parent = tf_decorator.unwrap(parent)

# A small helper method to construct members(children) protos.
def _AddMember(member_name, member_obj, proto):
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

parent_corner_cases = _CORNER_CASES.get(path, {})

if path not in _CORNER_CASES or parent_corner_cases:
    # Decide if we have a module or a class.
    if tf_inspect.ismodule(parent):
        # Create a module object.
        module_obj = api_objects_pb2.TFAPIModule()
        for name, child in children:
            if name in parent_corner_cases:
                # If we have an empty entry, skip this object.
                if parent_corner_cases[name]:
                    module_obj.member.add(**(parent_corner_cases[name]))
            else:
                _AddMember(name, child, module_obj)

        # Store the constructed module object.
        self._protos[lib_path] = api_objects_pb2.TFAPIObject(
            path=lib_path, tf_module=module_obj)
    elif _IsProtoClass(parent):
        proto_obj = api_objects_pb2.TFAPIProto()
        parent.DESCRIPTOR.CopyToProto(proto_obj.descriptor)

        # Store the constructed proto object.
        self._protos[lib_path] = api_objects_pb2.TFAPIObject(
            path=lib_path, tf_proto=proto_obj)
    elif tf_inspect.isclass(parent):
        # Construct a class.
        class_obj = api_objects_pb2.TFAPIClass()
        class_obj.is_instance.extend(
            _NormalizeIsInstance(i) for i in _SanitizedMRO(parent))
        for name, child in children:
            if name in parent_corner_cases:
                # If we have an empty entry, skip this object.
                if parent_corner_cases[name]:
                    class_obj.member.add(**(parent_corner_cases[name]))
            else:
                _AddMember(name, child, class_obj)

        # Store the constructed class object.
        self._protos[lib_path] = api_objects_pb2.TFAPIObject(
            path=lib_path, tf_class=class_obj)
    else:
        logging.error(
            'Illegal call to ApiProtoDump::_py_obj_to_proto.'
            'Object is neither a module nor a class: %s', path)
