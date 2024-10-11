import numpy as np # pragma: no cover
from pandas.core.dtypes.dtypes import DatetimeTZDtype, ExtensionDtype # pragma: no cover
from pandas.core.arrays import DatetimeArray # pragma: no cover
from pandas.api.types import is_dtype_equal # pragma: no cover
from typing import cast # pragma: no cover

ArrayLike = np.ndarray # pragma: no cover
upcasted_na = np.nan # pragma: no cover
empty_dtype = np.dtype('float64') # pragma: no cover
is_1d_only_ea_dtype = lambda dtype: dtype.kind in {'M', 'm', 'O', 'c'} # pragma: no cover
algos = type('Mock', (object,), {'take_nd': lambda values, indexer, axis: values.take(indexer, axis=axis)}) # pragma: no cover
self = type('Mock', (object,), {'block': type('Mock', (object,), {'dtype': np.dtype('float64'), 'fill_value': np.nan, 'values': np.array([1, 2, 3]), '_can_consolidate': True, 'astype': lambda dtype: type('Mock', (object,), {'values': np.array([None, None, None], dtype='object')})()}), 'shape': (1, 3), 'indexers': {0: np.array([0, 1, 2])}, '_is_valid_na_for': lambda dtype: True})() # pragma: no cover

import numpy as np # pragma: no cover
from pandas.core.dtypes.dtypes import DatetimeTZDtype, ExtensionDtype # pragma: no cover
from pandas.core.arrays import DatetimeArray # pragma: no cover
from pandas.api.types import is_dtype_equal # pragma: no cover
from typing import cast # pragma: no cover

ArrayLike = np.ndarray # pragma: no cover
upcasted_na = np.nan # pragma: no cover
empty_dtype = np.dtype('float64') # pragma: no cover
is_1d_only_ea_dtype = lambda dtype: dtype.kind in {'M', 'm', 'O', 'c'} # pragma: no cover
algos = type('Mock', (object,), {'take_nd': lambda values, indexer, axis: values.take(indexer, axis=axis)}) # pragma: no cover
self = type('Mock', (object,), {'block': type('Mock', (object,), {'dtype': np.dtype('float64'), 'fill_value': np.nan, 'values': np.array([1, 2, 3]), '_can_consolidate': True, 'astype': lambda self, dtype: type('Mock', (object,), {'values': np.array([None, None, None], dtype='object')})()}), 'shape': (1, 3), 'indexers': {0: np.array([0, 1, 2])}, '_is_valid_na_for': lambda self, dtype: True})() # pragma: no cover

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
