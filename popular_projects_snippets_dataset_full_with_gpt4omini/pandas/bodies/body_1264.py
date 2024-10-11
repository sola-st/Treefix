# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py
# Construct a DataFrame where each row is a random slice from 'letters'
idxs = np.random.randint(len(letters), size=(nobs, 2))
idxs.sort(axis=1)
strings = [letters[x[0] : x[1]] for x in idxs]

exit(DataFrame(strings, columns=["letters"]))
