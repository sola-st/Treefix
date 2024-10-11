# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Extracts `attrs`, `inputs`, and `input_types` in _apply_op_helper."""
inferred_from = {}
for input_arg in op_def.input_arg:
    input_name = input_arg.name
    if input_name in keywords:
        values = keywords.pop(input_name)
    elif input_name + "_" in keywords:
        # Handle the case where the name is a keyword or built-in
        # for Python so we use the name + _ instead.
        input_name += "_"
        values = keywords.pop(input_name)
    else:
        raise TypeError(f"No argument for input {input_name} found in {op_def}")

    # Goals:
    # * Convert values to Tensors if it contains constants.
    # * Verify that values is a list if that matches the input_arg's
    #   type.
    # * If the input_arg's type is determined by attrs, either set
    #   those attrs and validate those attr values are legal (if
    #   they have not yet been set) or validate the input matches
    #   the type indicated by the attrs (if they have already been
    #   inferred via an earlier input).
    # * If the input_arg has an explicit type, make sure the input
    #   conforms.

    if _IsListParameter(input_arg):
        if not _IsListValue(values):
            raise TypeError(
                f"Expected list for '{input_name}' argument to '{op_type_name}' "
                f"Op, not {values}.")
        # In cases where we expect all elements of the list to have the
        # same dtype, try to cast non-Tensor elements to that type.
        dtype = None
        default_dtype = None
        if input_arg.type != types_pb2.DT_INVALID:
            dtype = input_arg.type
        elif input_arg.number_attr:
            if input_arg.type_attr in attrs:
                dtype = attrs[input_arg.type_attr]
            else:
                for t in values:
                    if isinstance(t, ops.Tensor):
                        dtype = t.dtype
                        break

        # dtype still not found, prefer using the default dtype
        # from the attr.
            if dtype is None and input_arg.type_attr in default_type_attr_map:
                default_dtype = default_type_attr_map[input_arg.type_attr]

        try:
            if not input_arg.is_ref and dtype:
                dtype = dtypes.as_dtype(dtype).base_dtype
            values = ops.internal_convert_n_to_tensor(
                values,
                name=input_arg.name,
                dtype=dtype if dtype else None,
                preferred_dtype=default_dtype,
                as_ref=input_arg.is_ref)
            all_types = set(v.dtype.base_dtype for v in values)
            if input_arg.number_attr and len(all_types) > 1:
                # All types should match.
                raise TypeError(f"Not all types matched for {input_arg.name} for "
                                f"{op_type_name}. Got {all_types}")
        except (TypeError, ValueError):
            # What types does the conversion function think values have?
            observed_types = []
            for value in values:
                try:
                    converted_value = ops.convert_to_tensor(
                        value, as_ref=input_arg.is_ref)
                    observed_types.append(converted_value.dtype.base_dtype.name)
                except (TypeError, ValueError):
                    observed_types.append("<NOT CONVERTIBLE TO TENSOR>")
            observed = ", ".join(observed_types)

            prefix = ("Tensors in list passed to '%s' of '%s' Op have types [%s]" %
                      (input_name, op_type_name, observed))
            if input_arg.number_attr:
                if input_arg.type != types_pb2.DT_INVALID:
                    raise TypeError(f"{prefix} that do not match expected type "
                                    f"{dtype.name}.")
                elif input_arg.type_attr in attrs:
                    raise TypeError(f"{prefix} that do not match type {dtype.name} "
                                    "inferred from earlier arguments.")
                else:
                    raise TypeError(f"{prefix} that don't all match.")
            else:
                raise TypeError(f"{prefix} that are invalid. Tensors: {values}")

        types = [x.dtype for x in values]
        inputs.extend(values)
    else:
        # In cases where we have an expected type, try to convert non-Tensor
        # arguments to that type.
        dtype = None
        default_dtype = None
        allowed_list = None
        if input_arg.type != types_pb2.DT_INVALID:
            dtype = input_arg.type
        elif input_arg.type_attr in attrs:
            dtype = attrs[input_arg.type_attr]
        elif input_arg.type_attr in default_type_attr_map:
            # The dtype could not be inferred solely from the inputs,
            # so we prefer the attr's default, so code that adds a new attr
            # with a default is backwards compatible.
            default_dtype = default_type_attr_map[input_arg.type_attr]
            allowed_list = allowed_list_attr_map.get(input_arg.type_attr)

        try:
            # First see if we can get a valid dtype with the default conversion
            # and see if it matches an allowed dtypes. Some ops like ConcatV2 may
            # not list allowed dtypes, in which case we should skip this.
            if dtype is None and allowed_list:
                inferred = None
                try:
                    inferred = ops.convert_to_tensor(
                        values, name=input_arg.name, as_ref=input_arg.is_ref)
                except TypeError as err:
                    # When converting a python object such as a list of Dimensions, we
                    # need a dtype to be specified, thus tensor conversion may throw
                    # an exception which we will ignore and try again below.
                    pass

                # If we did not match an allowed dtype, try again with the default
                # dtype. This could be because we have an empty tensor and thus we
                # picked the wrong type.
                if inferred is not None and inferred.dtype in allowed_list:
                    values = inferred
                else:
                    values = ops.convert_to_tensor(
                        values,
                        name=input_arg.name,
                        as_ref=input_arg.is_ref,
                        preferred_dtype=default_dtype)
            else:
                values = ops.convert_to_tensor(
                    values,
                    name=input_arg.name,
                    dtype=dtype,
                    as_ref=input_arg.is_ref,
                    preferred_dtype=default_dtype)
        except TypeError as err:
            if dtype is None:
                raise err
            else:
                raise TypeError(
                    f"Expected {dtypes.as_dtype(dtype).name} passed to parameter "
                    f"'{input_arg.name}' of op '{op_type_name}', got "
                    f"{repr(values)} of type '{type(values).__name__}' instead. "
                    f"Error: {err}")
        except ValueError:
            # What type does convert_to_tensor think it has?
            try:
                observed = ops.convert_to_tensor(
                    values, as_ref=input_arg.is_ref).dtype.name
            except ValueError as err:
                raise ValueError(
                    f"Tried to convert '{input_name}' to a tensor and failed. "
                    f"Error: {err}")
            prefix = ("Input '%s' of '%s' Op has type %s that does not match" %
                      (input_name, op_type_name, observed))
            if input_arg.type != types_pb2.DT_INVALID:
                raise TypeError(f"{prefix} expected type of "
                                f"{dtypes.as_dtype(input_arg.type).name}.")
            else:
                # Update the maps with the default, if needed.
                k = input_arg.type_attr
                if k in default_type_attr_map:
                    if k not in attrs:
                        attrs[k] = default_type_attr_map[k]
                        if k not in inferred_from:
                            inferred_from[k] = "Default in OpDef"

                raise TypeError(
                    f"{prefix} type "
                    f"{dtypes.as_dtype(attrs[input_arg.type_attr]).name} of "
                    f"argument '{inferred_from[input_arg.type_attr]}'.")

        types = [values.dtype]
        inputs.append(values)
    base_types = [x.base_dtype for x in types]

    if input_arg.number_attr:
        # <number-attr> * <type> or <number-attr> * <type-attr>
        if input_arg.number_attr in attrs:
            if len(values) != attrs[input_arg.number_attr]:
                raise ValueError(
                    f"List argument '{input_name}' to '{op_type_name}' Op with "
                    f"length {len(values)} must match length "
                    f"{attrs[input_arg.number_attr]} of argument "
                    f"'{inferred_from[input_arg.number_attr]}'.")
        else:
            attrs[input_arg.number_attr] = len(values)
            inferred_from[input_arg.number_attr] = input_name
            num_attr = _Attr(op_def, input_arg.number_attr)
            if num_attr.has_minimum and len(values) < num_attr.minimum:
                raise ValueError(
                    f"List argument '{input_name}' to '{op_type_name}' Op with "
                    f"length {len(values)} shorter than minimum length "
                    f"{num_attr.minimum}.")
      # All tensors must have the same base type.
        if any(bt != base_types[0] for bt in base_types):
            raise TypeError(
                f"All tensors passed to '{input_name}' of '{op_type_name}' Op "
                f"must have the same type. Got {base_types} instead.")
        if input_arg.type != types_pb2.DT_INVALID:
            # <number-attr> * <type> case
            if base_types and base_types[0] != input_arg.type:
                assert False, "Unreachable"
        elif input_arg.type_attr in attrs:
            # <number-attr> * <type-attr> case, where <type-attr> already
            # has an inferred value.
            if base_types and base_types[0] != attrs[input_arg.type_attr]:
                assert False, "Unreachable"
        else:
            # <number-attr> * <type-attr> case, where we are now setting
            # the <type-attr> based on this input
            if not base_types:
                # If it's in default_type_attr_map, then wait to set it
                # (in "process remaining attrs", below).
                if input_arg.type_attr not in default_type_attr_map:
                    raise TypeError(
                        "Don't know how to infer type variable from empty input "
                        f"list passed to input '{input_name}' of '{op_type_name}' "
                        "Op.")
            else:
                attrs[input_arg.type_attr] = base_types[0]
                inferred_from[input_arg.type_attr] = input_name
                type_attr = _Attr(op_def, input_arg.type_attr)
                _SatisfiesTypeConstraint(
                    base_types[0], type_attr, param_name=input_name)
    elif input_arg.type_attr:
        # <type-attr>
        attr_value = base_types[0]
        if input_arg.type_attr in attrs:
            if attrs[input_arg.type_attr] != attr_value:
                raise TypeError(
                    f"Input '{input_name}' of '{op_type_name}' Op has type "
                    f"{dtypes.as_dtype(attr_value).name} that does not match type "
                    f"{dtypes.as_dtype(attrs[input_arg.type_attr]).name} of "
                    f"argument '{inferred_from[input_arg.type_attr]}'.")
        else:
            for base_type in base_types:
                _SatisfiesTypeConstraint(
                    base_type,
                    _Attr(op_def, input_arg.type_attr),
                    param_name=input_name)
            attrs[input_arg.type_attr] = attr_value
            inferred_from[input_arg.type_attr] = input_name
    elif input_arg.type_list_attr:
        # <type-list-attr>
        attr_value = base_types
        if input_arg.type_list_attr in attrs:
            if attrs[input_arg.type_list_attr] != attr_value:
                actual_types = ", ".join(dtypes.as_dtype(x).name for x in attr_value)
                expected_types = ", ".join(
                    dtypes.as_dtype(x).name for x in attrs[input_arg.type_list_attr])
                raise TypeError(
                    f"Input '{input_name}' of '{op_type_name}' Op has type list of "
                    f"{actual_types} that does not match type list {expected_types}"
                    f" of argument '{inferred_from[input_arg.type_list_attr]}'.")
        else:
            for base_type in base_types:
                _SatisfiesTypeConstraint(
                    base_type,
                    _Attr(op_def, input_arg.type_list_attr),
                    param_name=input_name)
            attrs[input_arg.type_list_attr] = attr_value
            inferred_from[input_arg.type_list_attr] = input_name
    else:
        # single Tensor with specified type
        if base_types[0] != input_arg.type:
            assert False, "Unreachable"

    if input_arg.is_ref:
        if not all(x._is_ref_dtype for x in types):  # pylint: disable=protected-access
            raise TypeError(
                f"'{op_type_name}' Op requires that input '{input_name}' be a "
                "mutable tensor (e.g.: a tf.Variable)")
        input_types.extend(types)
    else:
        input_types.extend(base_types)
