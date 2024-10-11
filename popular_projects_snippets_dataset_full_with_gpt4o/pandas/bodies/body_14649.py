# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
# GH2980
import matplotlib.pyplot as plt

n = 80
df = DataFrame(
    {
        "Clinical": np.random.choice([0, 1, 2, 3], n),
        "Confirmed": np.random.choice([0, 1, 2, 3], n),
        "Discarded": np.random.choice([0, 1, 2, 3], n),
    },
    index=np.arange(0, n),
)
ax = df.plot(kind="bar", stacked=True)
assert [int(x.get_text()) for x in ax.get_xticklabels()] == df.index.to_list()
ax.set_xticks(np.arange(0, 80, 10))
plt.draw()  # Update changes
assert [int(x.get_text()) for x in ax.get_xticklabels()] == list(
    np.arange(0, 80, 10)
)
