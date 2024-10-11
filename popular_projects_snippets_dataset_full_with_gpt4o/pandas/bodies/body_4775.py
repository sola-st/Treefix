# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
idx = Index(["ＡＢＣ", "１２３", "ｱｲｴ"])
expected = Index(["ABC", "123", "アイエ"])
result = idx.str.normalize("NFKC")
tm.assert_index_equal(result, expected)
