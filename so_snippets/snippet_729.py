# Extracted from https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
d = {320:1, 321:0, 322:3, 323:0}
print ', '.join(str(key) for min_value in (min(d.values()),) for key in d if d[key]==min_value)

"""Output:
321, 323
"""

