# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
df = DataFrame(
    {
        "clé1": ["a", "a", "b", "b", "a"],
        "clé2": ["1er", "2ème", "1er", "2ème", "1er"],
        "données1": np.random.randn(5),
        "données2": np.random.randn(5),
    }
)

# it works
df.pivot_table(index=["clé1"], columns=["clé2"])._repr_html_()
