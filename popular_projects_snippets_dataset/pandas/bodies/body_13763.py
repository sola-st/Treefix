# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 43305
df = DataFrame(index=MultiIndex.from_product([["A"], [0, 1]], names=[None, "one"]))
expected = dedent(
    """\
    >
      <thead>
        <tr>
          <th class="index_name level0" >&nbsp;</th>
          <th class="index_name level1" >one</th>
        </tr>
      </thead>
    """
)
assert expected in df.style.to_html()
