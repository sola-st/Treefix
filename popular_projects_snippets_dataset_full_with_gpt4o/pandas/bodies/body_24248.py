# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
with subprocess.Popen(
    ["pbpaste", "r"], stdout=subprocess.PIPE, close_fds=True
) as p:
    stdout = p.communicate()[0]
exit(stdout.decode(ENCODING))
