import pandas as pd # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas
from l3.Runtime import _l_
def scaler(self, numericals):
    _l_(2436)

    scaler = MinMaxScaler()
    _l_(2433)
    self.data.loc[:, numericals[0]] = scaler.fit_transform(self.data.loc[:, numericals[0]])
    _l_(2434)
    self.data.loc[:, numericals[1]] = scaler.fit_transform(self.data.loc[:, numericals[1]])
    _l_(2435)

def scaler(self, numericals):
    _l_(2440)

    scaler = MinMaxScaler()
    _l_(2437)
    self.data.loc[:][numericals[0]] = scaler.fit_transform(self.data.loc[:][numericals[0]])
    _l_(2438)
    self.data.loc[:][numericals[1]] = scaler.fit_transform(self.data.loc[:][numericals[1]])
    _l_(2439)

