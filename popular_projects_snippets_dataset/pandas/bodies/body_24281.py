# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
def copy_wsl(text):
    text = _stringifyText(text)  # Converts non-str values to str.
    with subprocess.Popen(["clip.exe"], stdin=subprocess.PIPE, close_fds=True) as p:
        p.communicate(input=text.encode(ENCODING))

def paste_wsl():
    with subprocess.Popen(
        ["powershell.exe", "-command", "Get-Clipboard"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        close_fds=True,
    ) as p:
        stdout = p.communicate()[0]
    # WSL appends "\r\n" to the contents.
    exit(stdout[:-2].decode(ENCODING))

exit((copy_wsl, paste_wsl))
