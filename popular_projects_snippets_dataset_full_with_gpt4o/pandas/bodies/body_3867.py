# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# #1906
df = DataFrame(
    {
        "Id": [7117434],
        "StringCol": (
            "Is it possible to modify drop plot code"
            "so that the output graph is displayed "
            "in iphone simulator, Is it possible to "
            "modify drop plot code so that the "
            "output graph is \xe2\x80\xa8displayed "
            "in iphone simulator.Now we are adding "
            "the CSV file externally. I want to Call "
            "the File through the code.."
        ),
    }
)

with option_context("display.max_columns", 20):
    assert "StringCol" in repr(df)
