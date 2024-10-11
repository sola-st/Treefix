# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
# issue-8193
# Test plot color dictionary format
data_files = ["a", "b"]

expected = [(0.5, 0.24, 0.6), (0.3, 0.7, 0.7)]

df1 = DataFrame(np.random.rand(2, 2), columns=data_files)
dic_color = {"b": (0.3, 0.7, 0.7), "a": (0.5, 0.24, 0.6)}

# Bar color test
ax = df1.plot(kind="bar", color=dic_color)
colors = [rect.get_facecolor()[0:-1] for rect in ax.get_children()[0:3:2]]
assert all(color == expected[index] for index, color in enumerate(colors))

# Line color test
ax = df1.plot(kind="line", color=dic_color)
colors = [rect.get_color() for rect in ax.get_lines()[0:2]]
assert all(color == expected[index] for index, color in enumerate(colors))
