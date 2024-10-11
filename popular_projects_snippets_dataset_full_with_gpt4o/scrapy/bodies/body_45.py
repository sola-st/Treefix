# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
if opts.profile:
    sys.stderr.write(f"scrapy: writing cProfile stats to {opts.profile!r}\n")
loc = locals()
p = cProfile.Profile()
p.runctx('cmd.run(args, opts)', globals(), loc)
if opts.profile:
    p.dump_stats(opts.profile)
