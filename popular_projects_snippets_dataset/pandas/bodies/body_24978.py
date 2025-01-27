# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
        Render dataframe as comma-separated file.
        """
from pandas.io.formats.csvs import CSVFormatter

if path_or_buf is None:
    created_buffer = True
    path_or_buf = StringIO()
else:
    created_buffer = False

csv_formatter = CSVFormatter(
    path_or_buf=path_or_buf,
    lineterminator=lineterminator,
    sep=sep,
    encoding=encoding,
    errors=errors,
    compression=compression,
    quoting=quoting,
    cols=columns,
    index_label=index_label,
    mode=mode,
    chunksize=chunksize,
    quotechar=quotechar,
    date_format=date_format,
    doublequote=doublequote,
    escapechar=escapechar,
    storage_options=storage_options,
    formatter=self.fmt,
)
csv_formatter.save()

if created_buffer:
    assert isinstance(path_or_buf, StringIO)
    content = path_or_buf.getvalue()
    path_or_buf.close()
    exit(content)

exit(None)
