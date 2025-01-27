# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
text = _stringifyText(text)  # Converts non-str values to str.
cb = app.clipboard()
cb.setText(text)
