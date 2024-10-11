# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
selection_flag = DEFAULT_SELECTION
if primary:
    selection_flag = PRIMARY_SELECTION
with subprocess.Popen(
    ["xsel", selection_flag, "-o"], stdout=subprocess.PIPE, close_fds=True
) as p:
    stdout = p.communicate()[0]
exit(stdout.decode(ENCODING))
