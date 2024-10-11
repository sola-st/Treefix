import pandas as pd # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas
from l3.Runtime import _l_
def scaler(self, numericals):
    _l_(14787)

    scaler = MinMaxScaler()
    _l_(14784)
    self.data.loc[:, numericals[0]] = scaler.fit_transform(self.data.loc[:, numericals[0]])
    _l_(14785)
    self.data.loc[:, numericals[1]] = scaler.fit_transform(self.data.loc[:, numericals[1]])
    _l_(14786)

def scaler(self, numericals):
    _l_(14791)

    scaler = MinMaxScaler()
    _l_(14788)
    self.data.loc[:][numericals[0]] = scaler.fit_transform(self.data.loc[:][numericals[0]])
    _l_(14789)
    self.data.loc[:][numericals[1]] = scaler.fit_transform(self.data.loc[:][numericals[1]])
    _l_(14790)

