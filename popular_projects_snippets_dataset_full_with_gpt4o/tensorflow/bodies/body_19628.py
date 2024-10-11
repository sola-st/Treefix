# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
c = self.baseConfigureTpuVersion()
c.configure_tpu_version('1.15')
paths = [call[0][0].full_url for call in urlopen.call_args_list]
self.assertCountEqual([
    'http://1.2.3.4:8475/requestversion/1.15?restartType=always',
    'http://5.6.7.8:8475/requestversion/1.15?restartType=always'
], sorted(paths))
