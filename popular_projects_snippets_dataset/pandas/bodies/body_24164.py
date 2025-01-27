# Extracted from ./data/repos/pandas/pandas/io/excel/_xlsxwriter.py
# Use the xlsxwriter module as the Excel writer.
from xlsxwriter import Workbook

engine_kwargs = combine_kwargs(engine_kwargs, kwargs)

if mode == "a":
    raise ValueError("Append mode is not supported with xlsxwriter!")

super().__init__(
    path,
    engine=engine,
    date_format=date_format,
    datetime_format=datetime_format,
    mode=mode,
    storage_options=storage_options,
    if_sheet_exists=if_sheet_exists,
    engine_kwargs=engine_kwargs,
)

self._book = Workbook(self._handles.handle, **engine_kwargs)
