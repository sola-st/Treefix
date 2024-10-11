# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
# GH: 40769
df = DataFrame(np.random.rand(10, 2))
import matplotlib.pyplot as plt

plt.style.use(scheme)
result = df.plot.box(return_type="dict")
for k, v in expected.items():
    assert result[k][0].get_color() == v
