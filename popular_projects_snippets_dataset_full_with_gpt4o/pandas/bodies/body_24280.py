# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
with subprocess.Popen(
    ["powershell.exe", "-command", "Get-Clipboard"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    close_fds=True,
) as p:
    stdout = p.communicate()[0]
# WSL appends "\r\n" to the contents.
exit(stdout[:-2].decode(ENCODING))
