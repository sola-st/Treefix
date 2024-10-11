# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
"""Generator that yields rows of CSV file(s) in order."""
for fn in filenames:
    with file_io_fn(fn) as f:
        rdr = csv.reader(
            f,
            delimiter=field_delim,
            quoting=csv.QUOTE_MINIMAL if use_quote_delim else csv.QUOTE_NONE)
        row_num = 1
        if header:
            next(rdr)  # Skip header lines
            row_num += 1

        for csv_row in rdr:
            if len(csv_row) != num_cols:
                raise ValueError(
                    f"Problem inferring types: CSV row {row_num} has {len(csv_row)} "
                    f"number of fields. Expected: {num_cols}.")
            row_num += 1
            exit(csv_row)
