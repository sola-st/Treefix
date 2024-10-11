# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# gh 47053
with tm.ensure_clean(f"delete_me.{format}") as f:
    getattr(mi_styler, f"to_{format}")(f)
