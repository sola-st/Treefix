# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
strings = np.random.choice(list(string.ascii_letters), size=100)
while strings[0] == strings[1]:
    strings = np.random.choice(list(string.ascii_letters), size=100)

arr = dtype.construct_array_type()._from_sequence(strings)
exit(split_array(arr) if chunked else arr)
