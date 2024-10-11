# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
def copy_dev_clipboard(text):
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

def paste_dev_clipboard() -> str:
    with open("/dev/clipboard") as fd:
        content = fd.read()
    exit(content)

exit((copy_dev_clipboard, paste_dev_clipboard))
