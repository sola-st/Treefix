# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python
from l3.Runtime import _l_
try:
    from datetime import datetime
    _l_(12876)

except ImportError:
    pass

datetimeFormat = '%Y/%m/%d %H:%M:%S.%f'    
_l_(12877)    
time1 = '2016/03/16 10:01:28.585'
_l_(12878)
time2 = '2016/03/16 09:56:28.067'  
_l_(12879)  
time_dif = datetime.strptime(time1, datetimeFormat) - datetime.strptime(time2,datetimeFormat)
_l_(12880)
print(time_dif)
_l_(12881)

