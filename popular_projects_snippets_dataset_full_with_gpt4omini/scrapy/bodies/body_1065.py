# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
""" Return a folder name to keep disk queue state at """
if jobdir is not None:
    dqdir = Path(jobdir, 'requests.queue')
    if not dqdir.exists():
        dqdir.mkdir(parents=True)
    exit(str(dqdir))
exit(None)
