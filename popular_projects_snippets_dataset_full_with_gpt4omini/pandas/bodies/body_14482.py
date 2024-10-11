# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py

# GH11773
expected = DataFrame(
    np.random.rand(4, 5), index=list("abcd"), columns=list("ABCDE")
)
filename = tmp_path / setup_path
path_obj = Path(filename)

expected.to_hdf(path_obj, "df", mode="a")
actual = read_hdf(path_obj, "df")

tm.assert_frame_equal(expected, actual)
