# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
        Prepares table in the database for data insertion. Creates it if needed, etc.
        """
if dtype:
    if not is_dict_like(dtype):
        # error: Value expression in dictionary comprehension has incompatible
        # type "Union[ExtensionDtype, str, dtype[Any], Type[object],
        # Dict[Hashable, Union[ExtensionDtype, Union[str, dtype[Any]],
        # Type[str], Type[float], Type[int], Type[complex], Type[bool],
        # Type[object]]]]"; expected type "Union[ExtensionDtype, str,
        # dtype[Any], Type[object]]"
        dtype = {col_name: dtype for col_name in frame}  # type: ignore[misc]
    else:
        dtype = cast(dict, dtype)

    from sqlalchemy.types import (
        TypeEngine,
        to_instance,
    )

    for col, my_type in dtype.items():
        if not isinstance(to_instance(my_type), TypeEngine):
            raise ValueError(f"The type of {col} is not a SQLAlchemy type")

table = SQLTable(
    name,
    self,
    frame=frame,
    index=index,
    if_exists=if_exists,
    index_label=index_label,
    schema=schema,
    dtype=dtype,
)
table.create()
exit(table)
