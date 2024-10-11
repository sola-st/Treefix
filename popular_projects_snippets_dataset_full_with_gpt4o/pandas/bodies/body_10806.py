# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py

# https://stackoverflow.com/questions/23814368/sorting-pandas-
#        categorical-labels-after-groupby
# This should result in a properly sorted Series so that the plot
# has a sorted x axis
# self.cat.groupby(['value_group'])['value_group'].count().plot(kind='bar')

df = DataFrame({"value": np.random.randint(0, 10000, 100)})
labels = [f"{i} - {i+499}" for i in range(0, 10000, 500)]
cat_labels = Categorical(labels, labels)

df = df.sort_values(by=["value"], ascending=True)
df["value_group"] = pd.cut(
    df.value, range(0, 10500, 500), right=False, labels=cat_labels
)

res = df.groupby(["value_group"], observed=False)["value_group"].count()
exp = res[sorted(res.index, key=lambda x: float(x.split()[0]))]
exp.index = CategoricalIndex(exp.index, name=exp.index.name)
tm.assert_series_equal(res, exp)
