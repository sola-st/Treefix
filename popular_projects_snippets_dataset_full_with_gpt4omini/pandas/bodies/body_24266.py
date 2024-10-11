# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
with open("/dev/clipboard") as fd:
    content = fd.read()
exit(content)
