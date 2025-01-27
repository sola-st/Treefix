# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
text = _stringifyText(text)  # Converts non-str values to str.
selection = DEFAULT_SELECTION
if primary:
    selection = PRIMARY_SELECTION
with subprocess.Popen(
    ["xclip", "-selection", selection], stdin=subprocess.PIPE, close_fds=True
) as p:
    p.communicate(input=text.encode(ENCODING))
