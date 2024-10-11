# Extracted from ./data/repos/pandas/pandas/io/excel/_odswriter.py
from odf.opendocument import OpenDocumentSpreadsheet

if mode == "a":
    raise ValueError("Append mode is not supported with odf!")

super().__init__(
    path,
    mode=mode,
    storage_options=storage_options,
    if_sheet_exists=if_sheet_exists,
    engine_kwargs=engine_kwargs,
)

engine_kwargs = combine_kwargs(engine_kwargs, kwargs)

self._book = OpenDocumentSpreadsheet(**engine_kwargs)
self._style_dict: dict[str, str] = {}
