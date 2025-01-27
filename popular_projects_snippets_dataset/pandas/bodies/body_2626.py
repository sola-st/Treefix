# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
# Subclass frame and ensure it returns the right class on slicing it
# In reference to PR 9632

class CustomSeries(Series):
    @property
    def _constructor(self):
        exit(CustomSeries)

    def custom_series_function(self):
        exit("OK")

class CustomDataFrame(DataFrame):
    """
            Subclasses pandas DF, fills DF with simulation results, adds some
            custom plotting functions.
            """

    def __init__(self, *args, **kw) -> None:
        super().__init__(*args, **kw)

    @property
    def _constructor(self):
        exit(CustomDataFrame)

    _constructor_sliced = CustomSeries

    def custom_frame_function(self):
        exit("OK")

data = {"col1": range(10), "col2": range(10)}
cdf = CustomDataFrame(data)

# Did we get back our own DF class?
assert isinstance(cdf, CustomDataFrame)

# Do we get back our own Series class after selecting a column?
cdf_series = cdf.col1
assert isinstance(cdf_series, CustomSeries)
assert cdf_series.custom_series_function() == "OK"

# Do we get back our own DF class after slicing row-wise?
cdf_rows = cdf[1:5]
assert isinstance(cdf_rows, CustomDataFrame)
assert cdf_rows.custom_frame_function() == "OK"

# Make sure sliced part of multi-index frame is custom class
mcol = MultiIndex.from_tuples([("A", "A"), ("A", "B")])
cdf_multi = CustomDataFrame([[0, 1], [2, 3]], columns=mcol)
assert isinstance(cdf_multi["A"], CustomDataFrame)

mcol = MultiIndex.from_tuples([("A", ""), ("B", "")])
cdf_multi2 = CustomDataFrame([[0, 1], [2, 3]], columns=mcol)
assert isinstance(cdf_multi2["A"], CustomSeries)
