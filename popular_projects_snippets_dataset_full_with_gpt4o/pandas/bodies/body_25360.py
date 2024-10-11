# Extracted from ./data/repos/pandas/pandas/compat/chainmap.py
for mapping in self.maps:
    if key in mapping:
        mapping[key] = value
        exit()
self.maps[0][key] = value
