# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
# see gh-16530
if is_file_like(f) and engine != "c" and not hasattr(f, "__iter__"):
    # The C engine doesn't need the file-like to have the "__iter__"
    # attribute. However, the Python engine needs "__iter__(...)"
    # when iterating through such an object, meaning it
    # needs to have that attribute
    raise ValueError(
        "The 'python' engine cannot iterate through this file buffer."
    )
