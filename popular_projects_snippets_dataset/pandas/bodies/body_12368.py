# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
data = DataFrame(
    {
        "fully_labelled": [1, 2, 3, 3, 1],
        "partially_labelled": [1.0, 2.0, np.nan, 9.0, np.nan],
        "Y": [7, 7, 9, 8, 10],
        "Z": pd.Categorical(["j", "k", "l", "k", "j"]),
    }
)

with tm.ensure_clean() as path:
    value_labels = {
        "fully_labelled": {1: "one", 2: "two", 3: "three"},
        "partially_labelled": {1.0: "one", 2.0: "two"},
    }
    expected = {**value_labels, "Z": {0: "j", 1: "k", 2: "l"}}

    writer = StataWriter(path, data, value_labels=value_labels)
    writer.write_file()

    with StataReader(path) as reader:
        reader_value_labels = reader.value_labels()
        assert reader_value_labels == expected

    msg = "Can't create value labels for notY, it wasn't found in the dataset."
    with pytest.raises(KeyError, match=msg):
        value_labels = {"notY": {7: "label1", 8: "label2"}}
        StataWriter(path, data, value_labels=value_labels)

    msg = (
        "Can't create value labels for Z, value labels "
        "can only be applied to numeric columns."
    )
    with pytest.raises(ValueError, match=msg):
        value_labels = {"Z": {1: "a", 2: "k", 3: "j", 4: "i"}}
        StataWriter(path, data, value_labels=value_labels)
