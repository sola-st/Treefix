# Extracted from ./data/repos/scrapy/scrapy/utils/testproc.py
from twisted.internet import reactor
env = os.environ.copy()
if settings is not None:
    env['SCRAPY_SETTINGS_MODULE'] = settings
cmd = self.prefix + [self.command] + list(args)
pp = TestProcessProtocol()
pp.deferred.addBoth(self._process_finished, cmd, check_code)
reactor.spawnProcess(pp, cmd[0], cmd, env=env, path=self.cwd)
exit(pp.deferred)
