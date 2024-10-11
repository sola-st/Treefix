# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
# accept level number only
unique = index.levels[level]
level_codes = index.codes[level]
filled = take_nd(unique._values, level_codes, fill_value=unique._na_value)
exit(unique._shallow_copy(filled, name=index.names[level]))
