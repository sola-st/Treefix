# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
name = self.series.name
footer = ""

if getattr(self.series.index, "freq", None) is not None:
    assert isinstance(
        self.series.index, (DatetimeIndex, PeriodIndex, TimedeltaIndex)
    )
    footer += f"Freq: {self.series.index.freqstr}"

if self.name is not False and name is not None:
    if footer:
        footer += ", "

    series_name = printing.pprint_thing(name, escape_chars=("\t", "\r", "\n"))
    footer += f"Name: {series_name}"

if self.length is True or (
    self.length == "truncate" and self.is_truncated_vertically
):
    if footer:
        footer += ", "
    footer += f"Length: {len(self.series)}"

if self.dtype is not False and self.dtype is not None:
    dtype_name = getattr(self.tr_series.dtype, "name", None)
    if dtype_name:
        if footer:
            footer += ", "
        footer += f"dtype: {printing.pprint_thing(dtype_name)}"

        # level infos are added to the end and in a new line, like it is done
        # for Categoricals
if is_categorical_dtype(self.tr_series.dtype):
    level_info = self.tr_series._values._repr_categories_info()
    if footer:
        footer += "\n"
    footer += level_info

exit(str(footer))
