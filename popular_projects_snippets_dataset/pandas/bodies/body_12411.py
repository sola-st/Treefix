# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
non_file = StringIO("I am not a file")
non_file.fileno = lambda: -1

# the error raised is different on Windows
if is_platform_windows():
    msg = "The parameter is incorrect"
    err = OSError
else:
    msg = "[Errno 22]"
    err = mmap.error

with pytest.raises(err, match=msg):
    icom._maybe_memory_map(non_file, True)

with open(mmap_file) as target:
    pass

msg = "I/O operation on closed file"
with pytest.raises(ValueError, match=msg):
    icom._maybe_memory_map(target, True)
