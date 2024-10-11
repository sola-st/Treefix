import numpy as np # pragma: no cover
from pandas.core.dtypes.dtypes import DatetimeTZDtype, ExtensionDtype # pragma: no cover
from pandas.core.arrays import DatetimeArray # pragma: no cover
from pandas.core.dtypes.common import is_1d_only_ea_dtype, is_dtype_equal # pragma: no cover
from pandas.core.algorithms import take_nd # pragma: no cover
from pandas._typing import ArrayLike # pragma: no cover
from typing import cast # pragma: no cover

class MockBlock: # pragma: no cover
    def __init__(self, dtype, values, fill_value, is_bool=False, can_consolidate=False): # pragma: no cover
        self.dtype = dtype # pragma: no cover
        self.values = values # pragma: no cover
        self.fill_value = fill_value # pragma: no cover
        self.is_bool = is_bool # pragma: no cover
        self._can_consolidate = can_consolidate # pragma: no cover
    def astype(self, dtype): # pragma: no cover
        return MockBlock(dtype, self.values.astype(dtype), self.fill_value) # pragma: no cover
 # pragma: no cover
class MockExtensionArray: # pragma: no cover
    @staticmethod # pragma: no cover
    def _from_sequence(sequence, dtype): # pragma: no cover
        return np.array(sequence, dtype=dtype) # pragma: no cover
    @staticmethod # pragma: no cover
    def _empty(shape, dtype): # pragma: no cover
        arr = np.empty(shape, dtype=dtype) # pragma: no cover
        return arr # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self, block, indexers, shape): # pragma: no cover
        self.block = block # pragma: no cover
        self.indexers = indexers # pragma: no cover
        self.shape = shape # pragma: no cover
    def _is_valid_na_for(self, dtype): # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
upcasted_na = np.datetime64('NaT') # pragma: no cover
empty_dtype = DatetimeTZDtype('ns', 'UTC') # pragma: no cover
block = MockBlock( # pragma: no cover
    dtype=np.dtype('object'), # pragma: no cover
    values=np.array([None, None], dtype=object), # pragma: no cover
    fill_value=None, # pragma: no cover
    is_bool=False, # pragma: no cover
    can_consolidate=False # pragma: no cover
) # pragma: no cover
self = MockSelf(block=block, indexers={}, shape=(1, 2)) # pragma: no cover
ExtensionDtype.construct_array_type = lambda self: MockExtensionArray # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
from l3.Runtime import _l_
values: ArrayLike
_l_(15501)

if upcasted_na is None and self.block.dtype.kind != "V":
    _l_(15537)

    # No upcasting is necessary
    fill_value = self.block.fill_value
    _l_(15502)
    values = self.block.values
    _l_(15503)
else:
    fill_value = upcasted_na
    _l_(15504)

    if self._is_valid_na_for(empty_dtype):
        _l_(15531)

        # note: always holds when self.block.dtype.kind == "V"
        blk_dtype = self.block.dtype
        _l_(15505)

        if blk_dtype == np.dtype("object"):
            _l_(15509)

            # we want to avoid filling with np.nan if we are
            # using None; we already know that we are all
            # nulls
            values = self.block.values.ravel(order="K")
            _l_(15506)
            if len(values) and values[0] is None:
                _l_(15508)

                fill_value = None
                _l_(15507)

        if isinstance(empty_dtype, DatetimeTZDtype):
            _l_(15530)

            # NB: exclude e.g. pyarrow[dt64tz] dtypes
            i8values = np.full(self.shape, fill_value.value)
            _l_(15510)
            aux = DatetimeArray(i8values, dtype=empty_dtype)
            _l_(15511)
            exit(aux)

        elif is_1d_only_ea_dtype(empty_dtype):
            _l_(15529)

            if is_dtype_equal(blk_dtype, empty_dtype) and self.indexers:
                _l_(15520)

                # avoid creating new empty array if we already have an array
                # with correct dtype that can be reindexed
                pass
                _l_(15512)
            else:
                empty_dtype = cast(ExtensionDtype, empty_dtype)
                _l_(15513)
                cls = empty_dtype.construct_array_type()
                _l_(15514)

                missing_arr = cls._from_sequence([], dtype=empty_dtype)
                _l_(15515)
                ncols, nrows = self.shape
                _l_(15516)
                assert ncols == 1, ncols
                _l_(15517)
                empty_arr = -1 * np.ones((nrows,), dtype=np.intp)
                _l_(15518)
                aux = missing_arr.take(
                    empty_arr, allow_fill=True, fill_value=fill_value
                )
                _l_(15519)
                exit(aux)
        elif isinstance(empty_dtype, ExtensionDtype):
            _l_(15528)

            # TODO: no tests get here, a handful would if we disabled
            #  the dt64tz special-case above (which is faster)
            cls = empty_dtype.construct_array_type()
            _l_(15521)
            missing_arr = cls._empty(shape=self.shape, dtype=empty_dtype)
            _l_(15522)
            missing_arr[:] = fill_value
            _l_(15523)
            aux = missing_arr
            _l_(15524)
            exit(aux)
        else:
            # NB: we should never get here with empty_dtype integer or bool;
            #  if we did, the missing_arr.fill would cast to gibberish
            missing_arr = np.empty(self.shape, dtype=empty_dtype)
            _l_(15525)
            missing_arr.fill(fill_value)
            _l_(15526)
            aux = missing_arr
            _l_(15527)
            exit(aux)

    if (not self.indexers) and (not self.block._can_consolidate):
        _l_(15533)

        aux = self.block.values
        _l_(15532)
        # preserve these for validation in concat_compat
        exit(aux)

    if self.block.is_bool:
        _l_(15536)

        # External code requested filling/upcasting, bool values must
        # be upcasted to object to avoid being upcasted to numeric.
        values = self.block.astype(np.dtype("object")).values
        _l_(15534)
    else:
        # No dtype upcasting is done here, it will be performed during
        # concatenation itself.
        values = self.block.values
        _l_(15535)

if not self.indexers:
    _l_(15541)

    # If there's no indexing to be done, we want to signal outside
    # code that this array must be copied explicitly.  This is done
    # by returning a view and checking `retval.base`.
    values = values.view()
    _l_(15538)

else:
    for ax, indexer in self.indexers.items():
        _l_(15540)

        values = algos.take_nd(values, indexer, axis=ax)
        _l_(15539)
aux = values
_l_(15542)

exit(aux)
