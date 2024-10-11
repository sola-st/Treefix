# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
pytest.importorskip(module)

path = os.path.join("~", "does_not_exist." + fn_ext)
monkeypatch.setattr(icom, "_expand_user", lambda x: os.path.join("foo", x))

msg1 = rf"File (b')?.+does_not_exist\.{fn_ext}'? does not exist"
msg2 = rf"\[Errno 2\] No such file or directory: '.+does_not_exist\.{fn_ext}'"
msg3 = "Unexpected character found when decoding 'false'"
msg4 = "path_or_buf needs to be a string file path or file-like"
msg5 = (
    rf"\[Errno 2\] File .+does_not_exist\.{fn_ext} does not exist: "
    rf"'.+does_not_exist\.{fn_ext}'"
)
msg6 = rf"\[Errno 2\] 没有那个文件或目录: '.+does_not_exist\.{fn_ext}'"
msg7 = (
    rf"\[Errno 2\] File o directory non esistente: '.+does_not_exist\.{fn_ext}'"
)
msg8 = rf"Failed to open local file.+does_not_exist\.{fn_ext}"

with pytest.raises(
    error_class,
    match=rf"({msg1}|{msg2}|{msg3}|{msg4}|{msg5}|{msg6}|{msg7}|{msg8})",
):
    reader(path)
