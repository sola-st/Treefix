# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
# GH 16748
df = DataFrame(
    {
        "cat": np.random.choice(list("abcde"), 100),
        "v": np.random.rand(100),
        "v1": np.random.rand(100),
    }
)
grouped = df.groupby("cat")

axes = _check_plot_works(
    grouped.boxplot, subplots=False, column=col, return_type="axes"
)

result_xticklabel = [x.get_text() for x in axes.get_xticklabels()]
assert expected_xticklabel == result_xticklabel
