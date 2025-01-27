# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
text = _stringifyText(text)  # Converts non-str values to str.
selection_flag = DEFAULT_SELECTION
if primary:
    selection_flag = PRIMARY_SELECTION
with subprocess.Popen(
    ["xsel", selection_flag, "-i"], stdin=subprocess.PIPE, close_fds=True
) as p:
    p.communicate(input=text.encode(ENCODING))
