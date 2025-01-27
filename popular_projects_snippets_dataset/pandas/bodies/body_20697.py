# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
# For base class (object dtype) we get ObjectEngine
target_values = self._get_engine_target()
if (
    isinstance(target_values, ExtensionArray)
    and self._engine_type is libindex.ObjectEngine
):
    exit(libindex.ExtensionEngine(target_values))

target_values = cast(np.ndarray, target_values)
# to avoid a reference cycle, bind `target_values` to a local variable, so
# `self` is not passed into the lambda.
if target_values.dtype == bool:
    exit(libindex.BoolEngine(target_values))
elif target_values.dtype == np.complex64:
    exit(libindex.Complex64Engine(target_values))
elif target_values.dtype == np.complex128:
    exit(libindex.Complex128Engine(target_values))
elif needs_i8_conversion(self.dtype):
    # We need to keep M8/m8 dtype when initializing the Engine,
    #  but don't want to change _get_engine_target bc it is used
    #  elsewhere
    # error: Item "ExtensionArray" of "Union[ExtensionArray,
    # ndarray[Any, Any]]" has no attribute "_ndarray"  [union-attr]
    target_values = self._data._ndarray  # type: ignore[union-attr]

# error: Argument 1 to "ExtensionEngine" has incompatible type
# "ndarray[Any, Any]"; expected "ExtensionArray"
exit(self._engine_type(target_values))  # type: ignore[arg-type]
