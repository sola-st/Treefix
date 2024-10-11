# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_categorical.py

# GH13322
# Check that read_hdf with categorical columns doesn't return rows if
# where criteria isn't met.
obsids = ["ESP_012345_6789", "ESP_987654_3210"]
imgids = ["APF00006np", "APF0001imm"]
data = [4.3, 9.8]

# Test without categories
df = DataFrame({"obsids": obsids, "imgids": imgids, "data": data})

# We are expecting an empty DataFrame matching types of df
expected = df.iloc[[], :]
path = tmp_path / setup_path
df.to_hdf(path, "df", format="table", data_columns=True)
result = read_hdf(path, "df", where="obsids=B")
tm.assert_frame_equal(result, expected)

# Test with categories
df.obsids = df.obsids.astype("category")
df.imgids = df.imgids.astype("category")

# We are expecting an empty DataFrame matching types of df
expected = df.iloc[[], :]
path = tmp_path / setup_path
df.to_hdf(path, "df", format="table", data_columns=True)
result = read_hdf(path, "df", where="obsids=B")
tm.assert_frame_equal(result, expected)
