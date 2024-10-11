import numpy as np # pragma: no cover
from pandas.core.arrays import ExtensionArray, DatetimeArray # pragma: no cover
from pandas.core.dtypes.dtypes import ExtensionDtype, DatetimeTZDtype # pragma: no cover
from pandas.core.dtypes.common import is_dtype_equal, is_1d_only_ea_dtype # pragma: no cover

class MockBlock:  # Mocking the Block class# pragma: no cover
    def __init__(self, dtype, values, fill_value=None, is_bool=False):# pragma: no cover
        self.dtype = np.dtype(dtype)# pragma: no cover
        self.values = np.array(values)# pragma: no cover
        self.fill_value = fill_value# pragma: no cover
        self.is_bool = is_bool# pragma: no cover
        self._can_consolidate = False# pragma: no cover
    @property# pragma: no cover
    def shape(self):# pragma: no cover
        return (len(self.values),) # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
self.block = MockBlock('object', [None, None, None], None) # pragma: no cover
self.indexers = {} # pragma: no cover
self.shape = self.block.shape # pragma: no cover
upcasted_na = None # pragma: no cover
empty_dtype = np.dtype('object') # pragma: no cover
self._is_valid_na_for = lambda x: True # pragma: no cover
algos = type('MockAlgos', (object,), {'take_nd': staticmethod(lambda arr, idx, axis: arr[idx])})() # pragma: no cover
cast = lambda x: x # pragma: no cover
is_1d_only_ea_dtype = lambda dtype: False # pragma: no cover
is_dtype_equal = lambda x, y: x == y # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
from l3.Runtime import _l_
values: ArrayLike
_l_(4209)

if upcasted_na is None and self.block.dtype.kind != "V":
    _l_(4245)

    # No upcasting is necessary
    fill_value = self.block.fill_value
    _l_(4210)
    values = self.block.values
    _l_(4211)
else:
    fill_value = upcasted_na
    _l_(4212)

    if self._is_valid_na_for(empty_dtype):
        _l_(4239)

        # note: always holds when self.block.dtype.kind == "V"
        blk_dtype = self.block.dtype
        _l_(4213)

        if blk_dtype == np.dtype("object"):
            _l_(4217)

            # we want to avoid filling with np.nan if we are
            # using None; we already know that we are all
            # nulls
            values = self.block.values.ravel(order="K")
            _l_(4214)
            if len(values) and values[0] is None:
                _l_(4216)

                fill_value = None
                _l_(4215)

        if isinstance(empty_dtype, DatetimeTZDtype):
            _l_(4238)

            # NB: exclude e.g. pyarrow[dt64tz] dtypes
            i8values = np.full(self.shape, fill_value.value)
            _l_(4218)
            aux = DatetimeArray(i8values, dtype=empty_dtype)
            _l_(4219)
            exit(aux)

        elif is_1d_only_ea_dtype(empty_dtype):
            _l_(4237)

            if is_dtype_equal(blk_dtype, empty_dtype) and self.indexers:
                _l_(4228)

                # avoid creating new empty array if we already have an array
                # with correct dtype that can be reindexed
                pass
                _l_(4220)
            else:
                empty_dtype = cast(ExtensionDtype, empty_dtype)
                _l_(4221)
                cls = empty_dtype.construct_array_type()
                _l_(4222)

                missing_arr = cls._from_sequence([], dtype=empty_dtype)
                _l_(4223)
                ncols, nrows = self.shape
                _l_(4224)
                assert ncols == 1, ncols
                _l_(4225)
                empty_arr = -1 * np.ones((nrows,), dtype=np.intp)
                _l_(4226)
                aux = missing_arr.take(
                    empty_arr, allow_fill=True, fill_value=fill_value
                )
                _l_(4227)
                exit(aux)
        elif isinstance(empty_dtype, ExtensionDtype):
            _l_(4236)

            # TODO: no tests get here, a handful would if we disabled
            #  the dt64tz special-case above (which is faster)
            cls = empty_dtype.construct_array_type()
            _l_(4229)
            missing_arr = cls._empty(shape=self.shape, dtype=empty_dtype)
            _l_(4230)
            missing_arr[:] = fill_value
            _l_(4231)
            aux = missing_arr
            _l_(4232)
            exit(aux)
        else:
            # NB: we should never get here with empty_dtype integer or bool;
            #  if we did, the missing_arr.fill would cast to gibberish
            missing_arr = np.empty(self.shape, dtype=empty_dtype)
            _l_(4233)
            missing_arr.fill(fill_value)
            _l_(4234)
            aux = missing_arr
            _l_(4235)
            exit(aux)

    if (not self.indexers) and (not self.block._can_consolidate):
        _l_(4241)

        aux = self.block.values
        _l_(4240)
        # preserve these for validation in concat_compat
        exit(aux)

    if self.block.is_bool:
        _l_(4244)

        # External code requested filling/upcasting, bool values must
        # be upcasted to object to avoid being upcasted to numeric.
        values = self.block.astype(np.dtype("object")).values
        _l_(4242)
    else:
        # No dtype upcasting is done here, it will be performed during
        # concatenation itself.
        values = self.block.values
        _l_(4243)

if not self.indexers:
    _l_(4249)

    # If there's no indexing to be done, we want to signal outside
    # code that this array must be copied explicitly.  This is done
    # by returning a view and checking `retval.base`.
    values = values.view()
    _l_(4246)

else:
    for ax, indexer in self.indexers.items():
        _l_(4248)

        values = algos.take_nd(values, indexer, axis=ax)
        _l_(4247)
aux = values
_l_(4250)

exit(aux)
