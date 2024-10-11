# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
index, data = tm.getMixedTypeDict()

# TODO(wesm), incomplete test?
indexed_frame = DataFrame(data, index=index)  # noqa
unindexed_frame = DataFrame(data)  # noqa

assert float_string_frame["foo"].dtype == np.object_
