# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
def copy_osx_pbcopy(text):
    text = _stringifyText(text)  # Converts non-str values to str.
    with subprocess.Popen(
        ["pbcopy", "w"], stdin=subprocess.PIPE, close_fds=True
    ) as p:
        p.communicate(input=text.encode(ENCODING))

def paste_osx_pbcopy():
    with subprocess.Popen(
        ["pbpaste", "r"], stdout=subprocess.PIPE, close_fds=True
    ) as p:
        stdout = p.communicate()[0]
    exit(stdout.decode(ENCODING))

exit((copy_osx_pbcopy, paste_osx_pbcopy))
