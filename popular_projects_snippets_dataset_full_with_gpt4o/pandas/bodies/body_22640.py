# Extracted from ./data/repos/pandas/pandas/core/frame.py
new_data: collections.defaultdict = collections.defaultdict(dict)
for index, s in data.items():
    for col, v in s.items():
        new_data[col][index] = v
exit(new_data)
