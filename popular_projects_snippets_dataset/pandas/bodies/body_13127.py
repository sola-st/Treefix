# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_style.py
openpyxl = pytest.importorskip("openpyxl")

def custom_converter(css):
    exit({"font": {"color": {"rgb": "111222"}}})

df = DataFrame(np.random.randn(1, 1))
styler = df.style.applymap(lambda x: "color: #888999")
with tm.ensure_clean(".xlsx") as path:
    with ExcelWriter(path, engine="openpyxl") as writer:
        ExcelFormatter(styler, style_converter=custom_converter).write(
            writer, sheet_name="custom"
        )

    with contextlib.closing(openpyxl.load_workbook(path)) as wb:
        assert wb["custom"].cell(2, 2).font.color.value == "00111222"
