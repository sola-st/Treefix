# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
values = ["\u03A1", "\u0391", "\u039D", "\u0394", "\u0391", "\u03A3"]

variable_labels_utf8 = {
    "a": "City Rank",
    "b": "City Exponent",
    "c": "".join(values),
}

msg = (
    "Variable labels must contain only characters that can be "
    "encoded in Latin-1"
)
with pytest.raises(ValueError, match=msg):
    with tm.ensure_clean() as path:
        mixed_frame.to_stata(path, variable_labels=variable_labels_utf8)

variable_labels_long = {
    "a": "City Rank",
    "b": "City Exponent",
    "c": "A very, very, very long variable label "
    "that is too long for Stata which means "
    "that it has more than 80 characters",
}

msg = "Variable labels must be 80 characters or fewer"
with pytest.raises(ValueError, match=msg):
    with tm.ensure_clean() as path:
        mixed_frame.to_stata(path, variable_labels=variable_labels_long)
