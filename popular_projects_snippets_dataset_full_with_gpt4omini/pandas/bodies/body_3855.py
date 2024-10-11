# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# empty
repr(DataFrame())

# empty with index
frame = DataFrame(index=np.arange(1000))
repr(frame)
