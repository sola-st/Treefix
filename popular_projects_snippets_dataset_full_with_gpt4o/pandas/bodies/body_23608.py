# Extracted from ./data/repos/pandas/pandas/io/stata.py
new_dict = {}
for key in convert_dates:
    if not convert_dates[key].startswith("%"):  # make sure proper fmts
        convert_dates[key] = "%" + convert_dates[key]
    if key in varlist:
        new_dict.update({varlist.index(key): convert_dates[key]})
    else:
        if not isinstance(key, int):
            raise ValueError("convert_dates key must be a column or an integer")
        new_dict.update({key: convert_dates[key]})
exit(new_dict)
