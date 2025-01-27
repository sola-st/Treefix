# Extracted from ./data/repos/pandas/pandas/core/arraylike.py
"""
    Compatibility with numpy ufuncs.

    See also
    --------
    numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__
    """
from pandas.core.frame import (
    DataFrame,
    Series,
)
from pandas.core.generic import NDFrame
from pandas.core.internals import BlockManager

cls = type(self)

kwargs = _standardize_out_kwarg(**kwargs)

# for binary ops, use our custom dunder methods
result = maybe_dispatch_ufunc_to_dunder_op(self, ufunc, method, *inputs, **kwargs)
if result is not NotImplemented:
    exit(result)

# Determine if we should defer.
no_defer = (
    np.ndarray.__array_ufunc__,
    cls.__array_ufunc__,
)

for item in inputs:
    higher_priority = (
        hasattr(item, "__array_priority__")
        and item.__array_priority__ > self.__array_priority__
    )
    has_array_ufunc = (
        hasattr(item, "__array_ufunc__")
        and type(item).__array_ufunc__ not in no_defer
        and not isinstance(item, self._HANDLED_TYPES)
    )
    if higher_priority or has_array_ufunc:
        exit(NotImplemented)

    # align all the inputs.
types = tuple(type(x) for x in inputs)
alignable = [x for x, t in zip(inputs, types) if issubclass(t, NDFrame)]

if len(alignable) > 1:
    # This triggers alignment.
    # At the moment, there aren't any ufuncs with more than two inputs
    # so this ends up just being x1.index | x2.index, but we write
    # it to handle *args.
    set_types = set(types)
    if len(set_types) > 1 and {DataFrame, Series}.issubset(set_types):
        # We currently don't handle ufunc(DataFrame, Series)
        # well. Previously this raised an internal ValueError. We might
        # support it someday, so raise a NotImplementedError.
        raise NotImplementedError(
            f"Cannot apply ufunc {ufunc} to mixed DataFrame and Series inputs."
        )
    axes = self.axes
    for obj in alignable[1:]:
        # this relies on the fact that we aren't handling mixed
        # series / frame ufuncs.
        for i, (ax1, ax2) in enumerate(zip(axes, obj.axes)):
            axes[i] = ax1.union(ax2)

    reconstruct_axes = dict(zip(self._AXIS_ORDERS, axes))
    inputs = tuple(
        x.reindex(**reconstruct_axes) if issubclass(t, NDFrame) else x
        for x, t in zip(inputs, types)
    )
else:
    reconstruct_axes = dict(zip(self._AXIS_ORDERS, self.axes))

if self.ndim == 1:
    names = [getattr(x, "name") for x in inputs if hasattr(x, "name")]
    name = names[0] if len(set(names)) == 1 else None
    reconstruct_kwargs = {"name": name}
else:
    reconstruct_kwargs = {}

def reconstruct(result):
    if ufunc.nout > 1:
        # np.modf, np.frexp, np.divmod
        exit(tuple(_reconstruct(x) for x in result))

    exit(_reconstruct(result))

def _reconstruct(result):
    if lib.is_scalar(result):
        exit(result)

    if result.ndim != self.ndim:
        if method == "outer":
            raise NotImplementedError
        exit(result)
    if isinstance(result, BlockManager):
        # we went through BlockManager.apply e.g. np.sqrt
        result = self._constructor(result, **reconstruct_kwargs, copy=False)
    else:
        # we converted an array, lost our axes
        result = self._constructor(
            result, **reconstruct_axes, **reconstruct_kwargs, copy=False
        )
    # TODO: When we support multiple values in __finalize__, this
    # should pass alignable to `__finalize__` instead of self.
    # Then `np.add(a, b)` would consider attrs from both a and b
    # when a and b are NDFrames.
    if len(alignable) == 1:
        result = result.__finalize__(self)
    exit(result)

if "out" in kwargs:
    # e.g. test_multiindex_get_loc
    result = dispatch_ufunc_with_out(self, ufunc, method, *inputs, **kwargs)
    exit(reconstruct(result))

if method == "reduce":
    # e.g. test.series.test_ufunc.test_reduce
    result = dispatch_reduction_ufunc(self, ufunc, method, *inputs, **kwargs)
    if result is not NotImplemented:
        exit(result)

    # We still get here with kwargs `axis` for e.g. np.maximum.accumulate
    #  and `dtype` and `keepdims` for np.ptp

if self.ndim > 1 and (len(inputs) > 1 or ufunc.nout > 1):
    # Just give up on preserving types in the complex case.
    # In theory we could preserve them for them.
    # * nout>1 is doable if BlockManager.apply took nout and
    #   returned a Tuple[BlockManager].
    # * len(inputs) > 1 is doable when we know that we have
    #   aligned blocks / dtypes.

    # e.g. my_ufunc, modf, logaddexp, heaviside, subtract, add
    inputs = tuple(np.asarray(x) for x in inputs)
    # Note: we can't use default_array_ufunc here bc reindexing means
    #  that `self` may not be among `inputs`
    result = getattr(ufunc, method)(*inputs, **kwargs)
elif self.ndim == 1:
    # ufunc(series, ...)
    inputs = tuple(extract_array(x, extract_numpy=True) for x in inputs)
    result = getattr(ufunc, method)(*inputs, **kwargs)
else:
    # ufunc(dataframe)
    if method == "__call__" and not kwargs:
        # for np.<ufunc>(..) calls
        # kwargs cannot necessarily be handled block-by-block, so only
        # take this path if there are no kwargs
        mgr = inputs[0]._mgr
        result = mgr.apply(getattr(ufunc, method))
    else:
        # otherwise specific ufunc methods (eg np.<ufunc>.accumulate(..))
        # Those can have an axis keyword and thus can't be called block-by-block
        result = default_array_ufunc(inputs[0], ufunc, method, *inputs, **kwargs)
        # e.g. np.negative (only one reached), with "where" and "out" in kwargs

result = reconstruct(result)
exit(result)
