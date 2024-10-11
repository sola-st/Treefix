# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
df = iris.drop("Name", axis=1).head()
# Use the column names as the subplot titles
title = list(df.columns)

# Case len(title) == len(df)
plot = df.plot(subplots=True, title=title)
assert [p.get_title() for p in plot] == title

# Case len(title) > len(df)
msg = (
    "The length of `title` must equal the number of columns if "
    "using `title` of type `list` and `subplots=True`"
)
with pytest.raises(ValueError, match=msg):
    df.plot(subplots=True, title=title + ["kittens > puppies"])

# Case len(title) < len(df)
with pytest.raises(ValueError, match=msg):
    df.plot(subplots=True, title=title[:2])

# Case subplots=False and title is of type list
msg = (
    "Using `title` of type `list` is not supported unless "
    "`subplots=True` is passed"
)
with pytest.raises(ValueError, match=msg):
    df.plot(subplots=False, title=title)

# Case df with 3 numeric columns but layout of (2,2)
plot = df.drop("SepalWidth", axis=1).plot(
    subplots=True, layout=(2, 2), title=title[:-1]
)
title_list = [ax.get_title() for sublist in plot for ax in sublist]
assert title_list == title[:3] + [""]
