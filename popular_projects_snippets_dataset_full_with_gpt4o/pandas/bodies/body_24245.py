# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
exit((
    subprocess.call(
        [WHICH_CMD, name], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    == 0
))
