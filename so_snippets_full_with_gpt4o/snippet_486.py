# Extracted from https://stackoverflow.com/questions/120656/directory-tree-listing-in-python
In [16]: Path('/etc').iterdir()
Out[16]: <generator object Path.iterdir at 0x110853fc0>

In [17]: [x.name for x in Path('/etc').iterdir()]
Out[17]:
['emond.d',
 'ntp-restrict.conf',
 'periodic',

In [18]: [x.name for x in Path('/etc').iterdir() if x.is_dir()]
Out[18]:
['emond.d',
 'periodic',
 'mach_init.d',

In [20]: [x.name for x in Path('/etc').glob('**/*.conf')]
Out[20]:
['ntp-restrict.conf',
 'dnsextd.conf',
 'syslog.conf',

In [23]: [x.name for x in Path('/etc').glob('**/*.conf') if x.stat().st_size > 1024]
Out[23]:
['dnsextd.conf',
 'pf.conf',
 'autofs.conf',

In [32]: Path('../Operational Metrics.md').resolve()
Out[32]: PosixPath('/Users/starver/code/xxxx/Operational Metrics.md')

In [10]: p = Path('.')

In [11]: core = p / 'web' / 'core'

In [13]: [x for x in core.iterdir() if x.is_file()]
Out[13]:
[PosixPath('web/core/metrics.py'),
 PosixPath('web/core/services.py'),
 PosixPath('web/core/querysets.py'),

