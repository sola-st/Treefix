# Extracted from ./data/repos/black/src/black/__init__.py
"""Reformat a single file under `src` without spawning child processes.

    `fast`, `write_back`, and `mode` options are passed to
    :func:`format_file_in_place` or :func:`format_stdin_to_stdout`.
    """
try:
    changed = Changed.NO

    if str(src) == "-":
        is_stdin = True
    elif str(src).startswith(STDIN_PLACEHOLDER):
        is_stdin = True
        # Use the original name again in case we want to print something
        # to the user
        src = Path(str(src)[len(STDIN_PLACEHOLDER) :])
    else:
        is_stdin = False

    if is_stdin:
        if src.suffix == ".pyi":
            mode = replace(mode, is_pyi=True)
        elif src.suffix == ".ipynb":
            mode = replace(mode, is_ipynb=True)
        if format_stdin_to_stdout(fast=fast, write_back=write_back, mode=mode):
            changed = Changed.YES
    else:
        cache: Cache = {}
        if write_back not in (WriteBack.DIFF, WriteBack.COLOR_DIFF):
            cache = read_cache(mode)
            res_src = src.resolve()
            res_src_s = str(res_src)
            if res_src_s in cache and cache[res_src_s] == get_cache_info(res_src):
                changed = Changed.CACHED
        if changed is not Changed.CACHED and format_file_in_place(
            src, fast=fast, write_back=write_back, mode=mode
        ):
            changed = Changed.YES
        if (write_back is WriteBack.YES and changed is not Changed.CACHED) or (
            write_back is WriteBack.CHECK and changed is Changed.NO
        ):
            write_cache(cache, [src], mode)
    report.done(src, changed)
except Exception as exc:
    if report.verbose:
        traceback.print_exc()
    report.failed(src, str(exc))
