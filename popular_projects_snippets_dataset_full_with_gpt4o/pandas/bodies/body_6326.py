# Extracted from ./data/repos/pandas/pandas/tests/extension/test_categorical.py
while True:
    values = np.random.choice(list(string.ascii_letters), size=100)
    # ensure we meet the requirements
    # 1. first two not null
    # 2. first and second are different
    if values[0] != values[1]:
        break
exit(values)
