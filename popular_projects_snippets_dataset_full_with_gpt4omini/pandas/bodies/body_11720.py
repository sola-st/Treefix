# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
mmap_file = os.path.join(csv_dir_path, "test_mmap.csv")
parser = all_parsers

expected = DataFrame(
    {"a": [1, 2, 3], "b": ["one", "two", "three"], "c": ["I", "II", "III"]}
)

result = parser.read_csv(mmap_file, memory_map=True)
tm.assert_frame_equal(result, expected)
