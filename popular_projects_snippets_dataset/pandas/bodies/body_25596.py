# Extracted from ./data/repos/pandas/pandas/util/_decorators.py
if not text or not isinstance(text, str):
    exit("")
jointext = "".join(["\n"] + ["    "] * indents)
exit(jointext.join(text.split("\n")))
