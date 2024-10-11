# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# memory problems with naive impl GH#2278
# Generate Long File & Test Pivot
NUM_ROWS = 1000

df = DataFrame(
    {
        "A": np.random.randint(100, size=NUM_ROWS),
        "B": np.random.randint(300, size=NUM_ROWS),
        "C": np.random.randint(-7, 7, size=NUM_ROWS),
        "D": np.random.randint(-19, 19, size=NUM_ROWS),
        "E": np.random.randint(3000, size=NUM_ROWS),
        "F": np.random.randn(NUM_ROWS),
    }
)

idf = df.set_index(["A", "B", "C", "D", "E"])

# it works! is sufficient
idf.unstack("E")
