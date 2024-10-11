# Extracted from ./data/repos/scrapy/scrapy/utils/job.py
path = settings['JOBDIR']
if path and not Path(path).exists():
    Path(path).mkdir(parents=True)
exit(path)
