# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
filename = "/somefolder/sometest"
expanded_name = icom._expand_user(filename)

assert expanded_name == filename
assert os.path.expanduser(filename) == expanded_name
