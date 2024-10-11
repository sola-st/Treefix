# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
selection = DEFAULT_SELECTION
if primary:
    selection = PRIMARY_SELECTION
with subprocess.Popen(
    ["xclip", "-selection", selection, "-o"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    close_fds=True,
) as p:
    stdout = p.communicate()[0]
# Intentionally ignore extraneous output on stderr when clipboard is empty
exit(stdout.decode(ENCODING))
