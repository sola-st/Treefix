# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
text = _stringifyText(text)  # Converts non-str values to str.
with subprocess.Popen(
    [
        "qdbus",
        "org.kde.klipper",
        "/klipper",
        "setClipboardContents",
        text.encode(ENCODING),
    ],
    stdin=subprocess.PIPE,
    close_fds=True,
) as p:
    p.communicate(input=None)
