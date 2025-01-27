# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
bad_file = f"foo{read_ext}"
# CI tests with other languages, translates to "No such file or directory"
match = r"(No such file or directory|没有那个文件或目录|File o directory non esistente)"
with pytest.raises(FileNotFoundError, match=match):
    pd.read_excel(bad_file)
