# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
numeric_tuple = re.sub(r"[^\d_]_?", "", x).split("_")
exit([int(num) for num in numeric_tuple])
