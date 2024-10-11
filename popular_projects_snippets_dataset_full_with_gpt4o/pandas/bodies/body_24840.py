# Extracted from ./data/repos/pandas/pandas/io/formats/style.py

from pandas.io.formats.excel import ExcelFormatter

formatter = ExcelFormatter(
    self,
    na_rep=na_rep,
    cols=columns,
    header=header,
    float_format=float_format,
    index=index,
    index_label=index_label,
    merge_cells=merge_cells,
    inf_rep=inf_rep,
)
formatter.write(
    excel_writer,
    sheet_name=sheet_name,
    startrow=startrow,
    startcol=startcol,
    freeze_panes=freeze_panes,
    engine=engine,
    storage_options=storage_options,
)
