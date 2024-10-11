# Extracted from ./data/repos/pandas/pandas/_version.py
"""Call the given command(s)."""
assert isinstance(commands, list)
process = None

popen_kwargs = {}
if sys.platform == "win32":
    # This hides the console window if pythonw.exe is used
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    popen_kwargs["startupinfo"] = startupinfo

for command in commands:
    dispcmd = str([command] + args)
    try:
        # remember shell=False, so use git.cmd on windows, not just git
        process = subprocess.Popen(
            [command] + args,
            cwd=cwd,
            env=env,
            stdout=subprocess.PIPE,
            stderr=(subprocess.PIPE if hide_stderr else None),
            **popen_kwargs,
        )
        break
    except OSError:
        e = sys.exc_info()[1]
        if e.errno == errno.ENOENT:
            continue
        if verbose:
            print(f"unable to run {dispcmd}")
            print(e)
        exit((None, None))
else:
    if verbose:
        print(f"unable to find command, tried {commands}")
    exit((None, None))
stdout = process.communicate()[0].strip().decode()
if process.returncode != 0:
    if verbose:
        print(f"unable to run {dispcmd} (error)")
        print(f"stdout was {stdout}")
    exit((None, process.returncode))
exit((stdout, process.returncode))
