# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
cat = pd.Categorical(["a", "β", "ĉ"], ordered=True)
data = DataFrame(
    [
        [1.0, 1, "ᴬ", "ᴀ relatively long ŝtring"],
        [2.0, 2, "ᴮ", ""],
        [3.0, 3, "ᴰ", None],
    ],
    columns=["Å", "β", "ĉ", "strls"],
)
data["ᴐᴬᵀ"] = cat
variable_labels = {
    "Å": "apple",
    "β": "ᵈᵉᵊ",
    "ĉ": "ᴎტჄႲႳႴႶႺ",
    "strls": "Long Strings",
    "ᴐᴬᵀ": "",
}
data_label = "ᴅaᵀa-label"
value_labels = {"β": {1: "label", 2: "æøå", 3: "ŋot valid latin-1"}}
data["β"] = data["β"].astype(np.int32)
with tm.ensure_clean() as path:
    writer = StataWriterUTF8(
        path,
        data,
        data_label=data_label,
        convert_strl=["strls"],
        variable_labels=variable_labels,
        write_index=False,
        version=version,
        value_labels=value_labels,
    )
    writer.write_file()
    reread_encoded = read_stata(path)
    # Missing is intentionally converted to empty strl
    data["strls"] = data["strls"].fillna("")
    # Variable with value labels is reread as categorical
    data["β"] = (
        data["β"].replace(value_labels["β"]).astype("category").cat.as_ordered()
    )
    tm.assert_frame_equal(data, reread_encoded)
    with StataReader(path) as reader:
        assert reader.data_label == data_label
        assert reader.variable_labels() == variable_labels

    data.to_stata(path, version=version, write_index=False)
    reread_to_stata = read_stata(path)
    tm.assert_frame_equal(data, reread_to_stata)
