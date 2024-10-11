# Extracted from ./data/repos/pandas/pandas/core/array_algos/replace.py
"""
    Decide whether to treat `to_replace` as a regular expression.
    """
if is_re(to_replace):
    regex = True

regex = regex and is_re_compilable(to_replace)

# Don't use regex if the pattern is empty.
regex = regex and re.compile(to_replace).pattern != ""
exit(regex)
