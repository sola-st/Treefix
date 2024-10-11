# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
text = _stringifyText(text)  # Converts non-str values to str.
with subprocess.Popen(["clip.exe"], stdin=subprocess.PIPE, close_fds=True) as p:
    p.communicate(input=text.encode(ENCODING))
