# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
if opts.profile:
    _run_command_profiled(cmd, args, opts)
else:
    cmd.run(args, opts)
