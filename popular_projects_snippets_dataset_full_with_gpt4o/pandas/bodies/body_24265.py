# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
text = _stringifyText(text)  # Converts non-str values to str.
if text == "":
    warnings.warn(
        "Pyperclip cannot copy a blank string to the clipboard on Cygwin. "
        "This is effectively a no-op.",
        stacklevel=find_stack_level(),
    )
if "\r" in text:
    warnings.warn(
        "Pyperclip cannot handle \\r characters on Cygwin.",
        stacklevel=find_stack_level(),
    )

with open("/dev/clipboard", "w") as fd:
    fd.write(text)
