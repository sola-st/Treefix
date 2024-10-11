# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
"""
    Support memory map for compressed files.

    GH 37621
    """
parser = all_parsers
expected = DataFrame({"a": [1], "b": [2]})

with tm.ensure_clean() as path:
    expected.to_csv(path, index=False, compression=compression)

    tm.assert_frame_equal(
        parser.read_csv(path, memory_map=True, compression=compression),
        expected,
    )
