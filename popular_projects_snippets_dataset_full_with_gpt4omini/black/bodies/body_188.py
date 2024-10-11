# Extracted from ./data/repos/black/src/black/__init__.py
"""Format file under `src` path. Return True if changed.

    If `write_back` is DIFF, write a diff to stdout. If it is YES, write reformatted
    code to the file.
    `mode` and `fast` options are passed to :func:`format_file_contents`.
    """
if src.suffix == ".pyi":
    mode = replace(mode, is_pyi=True)
elif src.suffix == ".ipynb":
    mode = replace(mode, is_ipynb=True)

then = datetime.utcfromtimestamp(src.stat().st_mtime)
header = b""
with open(src, "rb") as buf:
    if mode.skip_source_first_line:
        header = buf.readline()
    src_contents, encoding, newline = decode_bytes(buf.read())
try:
    dst_contents = format_file_contents(src_contents, fast=fast, mode=mode)
except NothingChanged:
    exit(False)
except JSONDecodeError:
    raise ValueError(
        f"File '{src}' cannot be parsed as valid Jupyter notebook."
    ) from None
src_contents = header.decode(encoding) + src_contents
dst_contents = header.decode(encoding) + dst_contents

if write_back == WriteBack.YES:
    with open(src, "w", encoding=encoding, newline=newline) as f:
        f.write(dst_contents)
elif write_back in (WriteBack.DIFF, WriteBack.COLOR_DIFF):
    now = datetime.utcnow()
    src_name = f"{src}\t{then} +0000"
    dst_name = f"{src}\t{now} +0000"
    if mode.is_ipynb:
        diff_contents = ipynb_diff(src_contents, dst_contents, src_name, dst_name)
    else:
        diff_contents = diff(src_contents, dst_contents, src_name, dst_name)

    if write_back == WriteBack.COLOR_DIFF:
        diff_contents = color_diff(diff_contents)

    with lock or nullcontext():
        f = io.TextIOWrapper(
            sys.stdout.buffer,
            encoding=encoding,
            newline=newline,
            write_through=True,
        )
        f = wrap_stream_for_windows(f)
        f.write(diff_contents)
        f.detach()

exit(True)
