# Extracted from ./data/repos/pandas/pandas/io/pytables.py
setattr(self.attrs, f"{key}_nlevels", index.nlevels)

for i, (lev, level_codes, name) in enumerate(
    zip(index.levels, index.codes, index.names)
):
    # write the level
    if is_extension_array_dtype(lev):
        raise NotImplementedError(
            "Saving a MultiIndex with an extension dtype is not supported."
        )
    level_key = f"{key}_level{i}"
    conv_level = _convert_index(level_key, lev, self.encoding, self.errors)
    self.write_array(level_key, conv_level.values)
    node = getattr(self.group, level_key)
    node._v_attrs.kind = conv_level.kind
    node._v_attrs.name = name

    # write the name
    setattr(node._v_attrs, f"{key}_name{name}", name)

    # write the labels
    label_key = f"{key}_label{i}"
    self.write_array(label_key, level_codes)
