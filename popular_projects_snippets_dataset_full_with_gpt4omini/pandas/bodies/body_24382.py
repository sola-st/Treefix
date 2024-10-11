# Extracted from ./data/repos/pandas/pandas/io/html.py
a = obj.find("a", href=True)
exit(None if not a else a["href"])
