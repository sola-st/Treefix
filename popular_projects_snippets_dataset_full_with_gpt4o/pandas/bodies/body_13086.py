# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
data.to_excel(path, header=header, merge_cells=merge_cells, index=index)

with ExcelFile(path) as xf:
    exit(pd.read_excel(
        xf, sheet_name=xf.sheet_names[0], header=parser_hdr
    ))
