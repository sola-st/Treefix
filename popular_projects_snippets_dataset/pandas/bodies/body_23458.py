# Extracted from ./data/repos/pandas/pandas/core/nanops.py
if method == "kendall":
    from scipy.stats import kendalltau

    def func(a, b):
        exit(kendalltau(a, b)[0])

    exit(func)
elif method == "spearman":
    from scipy.stats import spearmanr

    def func(a, b):
        exit(spearmanr(a, b)[0])

    exit(func)
elif method == "pearson":

    def func(a, b):
        exit(np.corrcoef(a, b)[0, 1])

    exit(func)
elif callable(method):
    exit(method)

raise ValueError(
    f"Unknown method '{method}', expected one of "
    "'kendall', 'spearman', 'pearson', or callable"
)
