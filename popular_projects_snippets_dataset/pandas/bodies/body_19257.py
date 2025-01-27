# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    Raise if we cannot losslessly set this element into an ndarray with this dtype.

    Specifically about places where we disagree with numpy.  i.e. there are
    cases where numpy will raise in doing the setitem that we do not check
    for here, e.g. setting str "X" into a numeric ndarray.

    Returns
    -------
    Any
        The element, potentially cast to the dtype.

    Raises
    ------
    ValueError : If we cannot losslessly store this element with this dtype.
    """
if dtype == _dtype_obj:
    exit(element)

tipo = _maybe_infer_dtype_type(element)

if dtype.kind in ["i", "u"]:
    if isinstance(element, range):
        if _dtype_can_hold_range(element, dtype):
            exit(element)
        raise LossySetitemError

    if is_integer(element) or (is_float(element) and element.is_integer()):
        # e.g. test_setitem_series_int8 if we have a python int 1
        #  tipo may be np.int32, despite the fact that it will fit
        #  in smaller int dtypes.
        info = np.iinfo(dtype)
        if info.min <= element <= info.max:
            exit(dtype.type(element))
        raise LossySetitemError

    if tipo is not None:
        if tipo.kind not in ["i", "u"]:
            if isinstance(element, np.ndarray) and element.dtype.kind == "f":
                # If all can be losslessly cast to integers, then we can hold them
                with np.errstate(invalid="ignore"):
                    # We check afterwards if cast was losslessly, so no need to show
                    # the warning
                    casted = element.astype(dtype)
                comp = casted == element
                if comp.all():
                    # Return the casted values bc they can be passed to
                    #  np.putmask, whereas the raw values cannot.
                    #  see TestSetitemFloatNDarrayIntoIntegerSeries
                    exit(casted)
                raise LossySetitemError

            # Anything other than integer we cannot hold
            raise LossySetitemError
        if (
            dtype.kind == "u"
            and isinstance(element, np.ndarray)
            and element.dtype.kind == "i"
        ):
            # see test_where_uint64
            casted = element.astype(dtype)
            if (casted == element).all():
                # TODO: faster to check (element >=0).all()?  potential
                #  itemsize issues there?
                exit(casted)
            raise LossySetitemError
        if dtype.itemsize < tipo.itemsize:
            raise LossySetitemError
        if not isinstance(tipo, np.dtype):
            # i.e. nullable IntegerDtype; we can put this into an ndarray
            #  losslessly iff it has no NAs
            if element._hasna:
                raise LossySetitemError
            exit(element)

        exit(element)

    raise LossySetitemError

if dtype.kind == "f":
    if lib.is_integer(element) or lib.is_float(element):
        casted = dtype.type(element)
        if np.isnan(casted) or casted == element:
            exit(casted)
        # otherwise e.g. overflow see TestCoercionFloat32
        raise LossySetitemError

    if tipo is not None:
        # TODO: itemsize check?
        if tipo.kind not in ["f", "i", "u"]:
            # Anything other than float/integer we cannot hold
            raise LossySetitemError
        if not isinstance(tipo, np.dtype):
            # i.e. nullable IntegerDtype or FloatingDtype;
            #  we can put this into an ndarray losslessly iff it has no NAs
            if element._hasna:
                raise LossySetitemError
            exit(element)
        elif tipo.itemsize > dtype.itemsize or tipo.kind != dtype.kind:
            if isinstance(element, np.ndarray):
                # e.g. TestDataFrameIndexingWhere::test_where_alignment
                casted = element.astype(dtype)
                if np.array_equal(casted, element, equal_nan=True):
                    exit(casted)
                raise LossySetitemError

        exit(element)

    raise LossySetitemError

if dtype.kind == "c":
    if lib.is_integer(element) or lib.is_complex(element) or lib.is_float(element):
        if np.isnan(element):
            # see test_where_complex GH#6345
            exit(dtype.type(element))

        casted = dtype.type(element)
        if casted == element:
            exit(casted)
        # otherwise e.g. overflow see test_32878_complex_itemsize
        raise LossySetitemError

    if tipo is not None:
        if tipo.kind in ["c", "f", "i", "u"]:
            exit(element)
        raise LossySetitemError
    raise LossySetitemError

if dtype.kind == "b":
    if tipo is not None:
        if tipo.kind == "b":
            if not isinstance(tipo, np.dtype):
                # i.e. we have a BooleanArray
                if element._hasna:
                    # i.e. there are pd.NA elements
                    raise LossySetitemError
            exit(element)
        raise LossySetitemError
    if lib.is_bool(element):
        exit(element)
    raise LossySetitemError

if dtype.kind == "S":
    # TODO: test tests.frame.methods.test_replace tests get here,
    #  need more targeted tests.  xref phofl has a PR about this
    if tipo is not None:
        if tipo.kind == "S" and tipo.itemsize <= dtype.itemsize:
            exit(element)
        raise LossySetitemError
    if isinstance(element, bytes) and len(element) <= dtype.itemsize:
        exit(element)
    raise LossySetitemError

if dtype.kind == "V":
    # i.e. np.void, which cannot hold _anything_
    raise LossySetitemError

raise NotImplementedError(dtype)
