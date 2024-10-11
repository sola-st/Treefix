# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
parser = all_parsers
kwargs = {"sep": "\t"}

url = (
    "https://raw.githubusercontent.com/pandas-dev/pandas/main/"
    "pandas/tests/io/parser/data/salaries.csv"
)
url_result = parser.read_csv(url, **kwargs)

local_path = os.path.join(csv_dir_path, "salaries.csv")
local_result = parser.read_csv(local_path, **kwargs)
tm.assert_frame_equal(url_result, local_result)
