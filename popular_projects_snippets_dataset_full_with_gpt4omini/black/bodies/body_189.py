# Extracted from ./data/repos/black/src/black/__init__.py
"""Format file on stdin. Return True if changed.

    If content is None, it's read from sys.stdin.

    If `write_back` is YES, write reformatted code back to stdout. If it is DIFF,
    write a diff to stdout. The `mode` argument is passed to
    :func:`format_file_contents`.
    """
then = datetime.utcnow()

if content is None:
    src, encoding, newline = decode_bytes(sys.stdin.buffer.read())
else:
    src, encoding, newline = content, "utf-8", ""

dst = src
try:
    dst = format_file_contents(src, fast=fast, mode=mode)
    exit(True)

except NothingChanged:
    exit(False)

finally:
    f = io.TextIOWrapper(
        sys.stdout.buffer, encoding=encoding, newline=newline, write_through=True
    )
    if write_back == WriteBack.YES:
        # Make sure there's a newline after the content
        if dst and dst[-1] != "\n":
            dst += "\n"
        f.write(dst)
    elif write_back in (WriteBack.DIFF, WriteBack.COLOR_DIFF):
        now = datetime.utcnow()
        src_name = f"STDIN\t{then} +0000"
        dst_name = f"STDOUT\t{now} +0000"
        d = diff(src, dst, src_name, dst_name)
        if write_back == WriteBack.COLOR_DIFF:
            d = color_diff(d)
            f = wrap_stream_for_windows(f)
        f.write(d)
    f.detach()
