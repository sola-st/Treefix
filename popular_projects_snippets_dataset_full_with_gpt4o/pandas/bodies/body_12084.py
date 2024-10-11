# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_network.py
# test reading compressed urls with various engines and
# extension inference
extension = _compression_to_extension[compression_only]
base_url = (
    "https://github.com/pandas-dev/pandas/raw/main/"
    "pandas/tests/io/parser/data/salaries.csv"
)

url = base_url + extension

if mode != "explicit":
    compression_only = mode

url_table = read_csv(url, sep="\t", compression=compression_only, engine=engine)
tm.assert_frame_equal(url_table, salaries_table)
