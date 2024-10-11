# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# big one
biggie = DataFrame(np.zeros((200, 4)), columns=range(4), index=range(200))
repr(biggie)
