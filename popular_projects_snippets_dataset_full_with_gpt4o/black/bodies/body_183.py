# Extracted from ./data/repos/black/src/black/__init__.py
"""The uncompromising code formatter."""
ctx.ensure_object(dict)

if src and code is not None:
    out(
        main.get_usage(ctx)
        + "\n\n'SRC' and 'code' cannot be passed simultaneously."
    )
    ctx.exit(1)
if not src and code is None:
    out(main.get_usage(ctx) + "\n\nOne of 'SRC' or 'code' is required.")
    ctx.exit(1)

root, method = (
    find_project_root(src, stdin_filename) if code is None else (None, None)
)
ctx.obj["root"] = root

if verbose:
    if root:
        out(
            f"Identified `{root}` as project root containing a {method}.",
            fg="blue",
        )

        normalized = [
            (
                (source, source)
                if source == "-"
                else (normalize_path_maybe_ignore(Path(source), root), source)
            )
            for source in src
        ]
        srcs_string = ", ".join(
            [
                (
                    f'"{_norm}"'
                    if _norm
                    else f'\033[31m"{source} (skipping - invalid)"\033[34m'
                )
                for _norm, source in normalized
            ]
        )
        out(f"Sources to be formatted: {srcs_string}", fg="blue")

    if config:
        config_source = ctx.get_parameter_source("config")
        user_level_config = str(find_user_pyproject_toml())
        if config == user_level_config:
            out(
                (
                    "Using configuration from user-level config at "
                    f"'{user_level_config}'."
                ),
                fg="blue",
            )
        elif config_source in (
            ParameterSource.DEFAULT,
            ParameterSource.DEFAULT_MAP,
        ):
            out("Using configuration from project root.", fg="blue")
        else:
            out(f"Using configuration in '{config}'.", fg="blue")
        if ctx.default_map:
            for param, value in ctx.default_map.items():
                out(f"{param}: {value}")

error_msg = "Oh no! 💥 💔 💥"
if (
    required_version
    and required_version != __version__
    and required_version != __version__.split(".")[0]
):
    err(
        f"{error_msg} The required version `{required_version}` does not match"
        f" the running version `{__version__}`!"
    )
    ctx.exit(1)
if ipynb and pyi:
    err("Cannot pass both `pyi` and `ipynb` flags!")
    ctx.exit(1)

write_back = WriteBack.from_configuration(check=check, diff=diff, color=color)
if target_version:
    versions = set(target_version)
else:
    # We'll autodetect later.
    versions = set()
mode = Mode(
    target_versions=versions,
    line_length=line_length,
    is_pyi=pyi,
    is_ipynb=ipynb,
    skip_source_first_line=skip_source_first_line,
    string_normalization=not skip_string_normalization,
    magic_trailing_comma=not skip_magic_trailing_comma,
    experimental_string_processing=experimental_string_processing,
    preview=preview,
    python_cell_magics=set(python_cell_magics),
)

if code is not None:
    # Run in quiet mode by default with -c; the extra output isn't useful.
    # You can still pass -v to get verbose output.
    quiet = True

report = Report(check=check, diff=diff, quiet=quiet, verbose=verbose)

if code is not None:
    reformat_code(
        content=code, fast=fast, write_back=write_back, mode=mode, report=report
    )
else:
    try:
        sources = get_sources(
            ctx=ctx,
            src=src,
            quiet=quiet,
            verbose=verbose,
            include=include,
            exclude=exclude,
            extend_exclude=extend_exclude,
            force_exclude=force_exclude,
            report=report,
            stdin_filename=stdin_filename,
        )
    except GitWildMatchPatternError:
        ctx.exit(1)

    path_empty(
        sources,
        "No Python files are present to be formatted. Nothing to do 😴",
        quiet,
        verbose,
        ctx,
    )

    if len(sources) == 1:
        reformat_one(
            src=sources.pop(),
            fast=fast,
            write_back=write_back,
            mode=mode,
            report=report,
        )
    else:
        from black.concurrency import reformat_many

        reformat_many(
            sources=sources,
            fast=fast,
            write_back=write_back,
            mode=mode,
            report=report,
            workers=workers,
        )

if verbose or not quiet:
    if code is None and (verbose or report.change_count or report.failure_count):
        out()
    out(error_msg if report.return_code else "All done! ✨ 🍰 ✨")
    if code is None:
        click.echo(str(report), err=True)
ctx.exit(report.return_code)
