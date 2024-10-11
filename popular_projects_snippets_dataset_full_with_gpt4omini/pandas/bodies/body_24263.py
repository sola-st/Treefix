# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
with subprocess.Popen(
    ["qdbus", "org.kde.klipper", "/klipper", "getClipboardContents"],
    stdout=subprocess.PIPE,
    close_fds=True,
) as p:
    stdout = p.communicate()[0]

# Workaround for https://bugs.kde.org/show_bug.cgi?id=342874
# TODO: https://github.com/asweigart/pyperclip/issues/43
clipboardContents = stdout.decode(ENCODING)
# even if blank, Klipper will append a newline at the end
assert len(clipboardContents) > 0
# make sure that newline is there
assert clipboardContents.endswith("\n")
if clipboardContents.endswith("\n"):
    clipboardContents = clipboardContents[:-1]
exit(clipboardContents)
