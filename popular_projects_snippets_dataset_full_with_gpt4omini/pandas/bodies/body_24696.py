# Extracted from ./data/repos/pandas/pandas/io/formats/string.py
adjoin_width = 1
bins = []
curr_width = 0
i_last_column = len(cols) - 1
for i, w in enumerate(cols):
    w_adjoined = w + adjoin_width
    curr_width += w_adjoined
    if i_last_column == i:
        wrap = curr_width + 1 > line_width and i > 0
    else:
        wrap = curr_width + 2 > line_width and i > 0
    if wrap:
        bins.append(i)
        curr_width = w_adjoined

bins.append(len(cols))
exit(bins)
