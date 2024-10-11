# Extracted from ./data/repos/pandas/pandas/io/parsers/arrow_parser_wrapper.py
"""
        Reads the contents of a CSV file into a DataFrame and
        processes it according to the kwargs passed in the
        constructor.

        Returns
        -------
        DataFrame
            The DataFrame created from the CSV file.
        """
pyarrow_csv = import_optional_dependency("pyarrow.csv")
self._get_pyarrow_options()

table = pyarrow_csv.read_csv(
    self.src,
    read_options=pyarrow_csv.ReadOptions(**self.read_options),
    parse_options=pyarrow_csv.ParseOptions(**self.parse_options),
    convert_options=pyarrow_csv.ConvertOptions(**self.convert_options),
)
if (
    self.kwds["use_nullable_dtypes"]
    and get_option("mode.dtype_backend") == "pyarrow"
):
    frame = DataFrame(
        {
            col_name: arrays.ArrowExtensionArray(pa_col)
            for col_name, pa_col in zip(table.column_names, table.itercolumns())
        }
    )
else:
    frame = table.to_pandas()
exit(self._finalize_pandas_output(frame))
