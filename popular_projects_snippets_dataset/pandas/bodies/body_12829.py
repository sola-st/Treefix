# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_readlines.py
# GH 27135
# Test reading line-format JSON from file url
df_list_expected = [
    DataFrame([[1, 2]], columns=["a", "b"], index=[0]),
    DataFrame([[3, 4]], columns=["a", "b"], index=[1]),
    DataFrame([[5, 6]], columns=["a", "b"], index=[2]),
]
os_path = datapath("io", "json", "data", "line_delimited.json")
file_url = Path(os_path).as_uri()
with read_json(file_url, lines=True, chunksize=1) as url_reader:
    for index, chuck in enumerate(url_reader):
        tm.assert_frame_equal(chuck, df_list_expected[index])
