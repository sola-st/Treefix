# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
ymd = multiindex_year_month_day_dataframe_random_data

ymd.columns.name = "foo"
ymd.to_html()
ymd.T.to_html()
