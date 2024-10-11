# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
use_east_asian_width = get_option("display.unicode.east_asian_width")
if use_east_asian_width:
    exit(EastAsianTextAdjustment())
else:
    exit(TextAdjustment())
