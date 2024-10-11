import numpy as np # pragma: no cover

ArrayLike = np.ndarray # pragma: no cover
upcasted_na = np.nan # pragma: no cover
class MockBlock:# pragma: no cover
    def __init__(self, dtype, fill_value, shape, values):# pragma: no cover
        self.dtype = dtype# pragma: no cover
        self.fill_value = fill_value# pragma: no cover
        self.shape = shape# pragma: no cover
        self.values = values# pragma: no cover
        self.is_bool = False# pragma: no cover
        self._can_consolidate = True# pragma: no cover
# pragma: no cover
    def astype(self, dtype):# pragma: no cover
        return self# pragma: no cover
# pragma: no cover
self = type('Mock', (object,), {})()# pragma: no cover
self.block = MockBlock(dtype=np.dtype('float64'), fill_value=np.nan, shape=(2, 2), values=np.array([[1.0, 2.0], [3.0, 4.0]])) # pragma: no cover
empty_dtype = np.dtype('float64') # pragma: no cover
class MockDatetimeTZDtype:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
DatetimeTZDtype = MockDatetimeTZDtype # pragma: no cover
class MockDatetimeArray:# pragma: no cover
    def __init__(self, values, dtype):# pragma: no cover
        self.values = values# pragma: no cover
        self.dtype = dtype# pragma: no cover
# pragma: no cover
DatetimeArray = MockDatetimeArray # pragma: no cover
def is_1d_only_ea_dtype(dtype):# pragma: no cover
    return dtype.ndim == 1# pragma: no cover
# pragma: no cover
is_1d_only_ea_dtype = is_1d_only_ea_dtype # pragma: no cover
def is_dtype_equal(dtype1, dtype2):# pragma: no cover
    return dtype1 == dtype2# pragma: no cover
# pragma: no cover
is_dtype_equal = is_dtype_equal # pragma: no cover
def cast(dtype, new_type):# pragma: no cover
    return new_type# pragma: no cover
# pragma: no cover
cast = cast # pragma: no cover
class MockAlgorithm:# pragma: no cover
    @staticmethod# pragma: no cover
    def take_nd(arr, indexer, axis):# pragma: no cover
        return arr[indexer]# pragma: no cover
# pragma: no cover
algos = MockAlgorithm # pragma: no cover
class MockExtensionDtype:# pragma: no cover
    @staticmethod# pragma: no cover
    def construct_array_type():# pragma: no cover
        return MockBlock(dtype=np.dtype('float64'), fill_value=np.nan, shape=(2, 2), values=np.array([[1.0, 2.0], [3.0, 4.0]]))# pragma: no cover
# pragma: no cover
ExtensionDtype = MockExtensionDtype # pragma: no cover

import numpy as np # pragma: no cover

ArrayLike = np.ndarray # pragma: no cover
upcasted_na = np.nan # pragma: no cover
class MockBlock:# pragma: no cover
    def __init__(self, dtype, fill_value, shape, values):# pragma: no cover
        self.dtype = dtype# pragma: no cover
        self.fill_value = fill_value# pragma: no cover
        self.shape = shape# pragma: no cover
        self.values = values# pragma: no cover
        self.is_bool = False# pragma: no cover
        self._can_consolidate = True# pragma: no cover
# pragma: no cover
    def astype(self, dtype):# pragma: no cover
        return self# pragma: no cover
# pragma: no cover
    def _is_valid_na_for(self, dtype):# pragma: no cover
        return True# pragma: no cover
# pragma: no cover
self = type('Mock', (object,), {})()# pragma: no cover
self.block = MockBlock(dtype=np.dtype('float64'), fill_value=np.nan, shape=(2, 2), values=np.array([[1.0, 2.0], [3.0, 4.0]])) # pragma: no cover
empty_dtype = np.dtype('float64') # pragma: no cover
class MockDatetimeTZDtype:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
DatetimeTZDtype = MockDatetimeTZDtype # pragma: no cover
class MockDatetimeArray:# pragma: no cover
    def __init__(self, values, dtype):# pragma: no cover
        self.values = values# pragma: no cover
        self.dtype = dtype# pragma: no cover
# pragma: no cover
DatetimeArray = MockDatetimeArray # pragma: no cover
def is_1d_only_ea_dtype(dtype):# pragma: no cover
    return dtype.ndim == 1# pragma: no cover
# pragma: no cover
is_1d_only_ea_dtype = is_1d_only_ea_dtype # pragma: no cover
def is_dtype_equal(dtype1, dtype2):# pragma: no cover
    return dtype1 == dtype2# pragma: no cover
# pragma: no cover
is_dtype_equal = is_dtype_equal # pragma: no cover
def cast(dtype, new_type):# pragma: no cover
    return new_type# pragma: no cover
# pragma: no cover
cast = cast # pragma: no cover
class MockAlgorithm:# pragma: no cover
    @staticmethod# pragma: no cover
    def take_nd(arr, indexer, axis):# pragma: no cover
        return arr[indexer]# pragma: no cover
# pragma: no cover
algos = MockAlgorithm # pragma: no cover
class MockExtensionDtype:# pragma: no cover
    @staticmethod# pragma: no cover
    def construct_array_type():# pragma: no cover
        return MockBlock(dtype=np.dtype('float64'), fill_value=np.nan, shape=(2, 2), values=np.array([[1.0, 2.0], [3.0, 4.0]]))# pragma: no cover
# pragma: no cover
ExtensionDtype = MockExtensionDtype # pragma: no cover

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
