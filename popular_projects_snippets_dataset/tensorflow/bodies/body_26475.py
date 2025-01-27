# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
"""Infers column names from first rows of files."""
csv_kwargs = {
    "delimiter": field_delim,
    "quoting": csv.QUOTE_MINIMAL if use_quote_delim else csv.QUOTE_NONE
}
with file_io_fn(filenames[0]) as f:
    try:
        column_names = next(csv.reader(f, **csv_kwargs))
    except StopIteration:
        raise ValueError("Failed when reading the header line of "
                         f"{filenames[0]}. Is it an empty file?")

for name in filenames[1:]:
    with file_io_fn(name) as f:
        try:
            if next(csv.reader(f, **csv_kwargs)) != column_names:
                raise ValueError(
                    "All input CSV files should have the same column names in the "
                    f"header row. File {name} has different column names.")
        except StopIteration:
            raise ValueError("Failed when reading the header line of "
                             f"{name}. Is it an empty file?")
exit(column_names)
