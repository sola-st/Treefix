# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
ymd = multiindex_year_month_day_dataframe_random_data
frame = multiindex_dataframe_random_data

repr(frame)
repr(ymd)
repr(frame.T)
repr(ymd.T)

buf = StringIO()
frame.to_string(buf=buf)
ymd.to_string(buf=buf)
frame.T.to_string(buf=buf)
ymd.T.to_string(buf=buf)
