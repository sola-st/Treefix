def mock_input(prompt): # pragma: no cover
    inputs = { # pragma: no cover
        'Enter The day :- ': '32',  # Will trigger uncovered 'Plz 1 To 30 value Enter ........' # pragma: no cover
        'Enter The Month :- ': '15',  # Will trigger uncovered 'Plz 1 To 12 value Enter ........' # pragma: no cover
        'Enter The Year :- ': '2023',  # Will break out of loop # pragma: no cover
        'Enter No. For Aday or SUBTRACT Days :: ': '0',  # Will trigger uncovered 'nd == 0' path # pragma: no cover
        'Enter Your Choice :: ': '2'  # Will trigger uncovered 'month-day-year' format # pragma: no cover
    } # pragma: no cover
    return inputs[prompt] # pragma: no cover
builtins.input = mock_input # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6871016/adding-days-to-a-date-in-python
from l3.Runtime import _l_
class myDate:
    _l_(14928)


    def __init__(self):
        _l_(14841)

        self.day = 0
        _l_(14820)
        self.month = 0
        _l_(14821)
        self.year = 0
        _l_(14822)
        ## for checking valid days month and year
        while (True):
            _l_(14828)

            d = int(input("Enter The day :- "))
            _l_(14823)
            if (d > 31):
                _l_(14827)

                print("Plz 1 To 30 value Enter ........")
                _l_(14824)
            else:
                self.day = d
                _l_(14825)
                break
                _l_(14826)

        while (True):
            _l_(14834)

            m = int(input("Enter The Month :- "))
            _l_(14829)
            if (m > 13):
                _l_(14833)

                print("Plz 1 To 12 value Enter ........")
                _l_(14830)
            else:
                self.month = m
                _l_(14831)
                break
                _l_(14832)

        while (True):
            _l_(14840)

            y = int(input("Enter The Year :- "))
            _l_(14835)
            if (y > 9999 and y < 0000):
                _l_(14839)

                print("Plz 0000 To 9999 value Enter ........")
                _l_(14836)
            else:
                self.year = y
                _l_(14837)
                break
                _l_(14838)
    ## method for aday ands cnttract days
    def adayDays(self, n):
        _l_(14916)

        ## aday days to date day
        nd = self.day + n
        _l_(14842)
        print(nd)
        _l_(14843)
        ## check days subtract from date
        if nd == 0:
            _l_(14915)

            if(self.year % 4 == 0):
                _l_(14852)

                if(self.month == 3):
                    _l_(14847)

                    self.day = 29
                    _l_(14844)
                    self.month -= 1
                    _l_(14845)
                    self.year = self. year
                    _l_(14846)
            else:
                if(self.month == 3):
                    _l_(14851)

                    self.day = 28
                    _l_(14848)
                    self.month -= 1
                    _l_(14849)
                    self.year = self. year
                    _l_(14850)
            if  (self.month == 5) or (self.month == 7) or (self.month == 8) or (self.month == 10) or (self.month == 12):
                _l_(14863)

                self.day = 30
                _l_(14853)
                self.month -= 1
                _l_(14854)
                self.year = self. year
                _l_(14855)
            elif (self.month == 2) or (self.month == 4) or (self.month == 6) or (self.month == 9) or (self.month == 11):
                _l_(14862)

                self.day = 31
                _l_(14856)
                self.month -= 1
                _l_(14857)
                self.year = self. year
                _l_(14858)

            elif(self.month == 1):
                _l_(14861)

                self.month = 12
                _l_(14859)
                self.year -= 1    
                _l_(14860)    
        ## nd == 0 if condition over
        ## after subtract days to day io goes into negative then
        elif nd < 0 :
            _l_(14914)

            n = abs(n)## return positive if no is negative
            _l_(14864)## return positive if no is negative
            for i in range (n,0,-1):
                _l_(14880)

                
                if self.day == 0:
                    _l_(14879)


                    if self.month == 1:
                        _l_(14877)

                        self.day = 30
                        _l_(14865)
                        
                        self.month = 12
                        _l_(14866)
                        self.year -= 1
                        _l_(14867)
                    else:
                        self.month -= 1
                        _l_(14868)
                        if(self.month == 1) or (self.month == 3)or (self.month == 5) or (self.month == 7) or (self.month == 8) or (self.month == 10) or (self.month ==12):
                            _l_(14876)

                            self.day = 30
                            _l_(14869)
                        elif(self.month == 4)or (self.month == 6) or (self.month == 9) or (self.month == 11):
                            _l_(14875)

                            self.day = 29
                            _l_(14870)
                        elif(self.month == 2):
                            _l_(14874)

                            if(self.year % 4 == 0):
                                _l_(14873)

                                self.day == 28
                                _l_(14871)
                            else:
                                self.day == 27
                                _l_(14872)
                else:
                    self.day -= 1
                    _l_(14878)

        ## enf of elif negative days
        ## adaying days to DATE
        else:
            cnt = 0
            _l_(14881)
            while (True):
                _l_(14913)


                if self.month == 2:
                    _l_(14912)

                    
                    if(self.year % 4 == 0):
                        _l_(14894)

                        if(nd > 29):
                            _l_(14887)

                            cnt = nd - 29
                            _l_(14882)
                            nd = cnt
                            _l_(14883)
                            self.month += 1
                            _l_(14884)
                        else:
                            self.day = nd
                            _l_(14885)
                            break
                            _l_(14886)
                ## if not leap year then
                    else:  
                    
                        if(nd > 28):
                            _l_(14893)

                            cnt = nd - 28
                            _l_(14888)
                            nd = cnt
                            _l_(14889)
                            self.month += 1
                            _l_(14890)
                        else:
                            self.day = nd
                            _l_(14891)
                            break
                            _l_(14892)
                ## checking month other than february month
                elif(self.month == 1) or (self.month == 3) or (self.month == 5) or (self.month == 7) or (self.month == 8) or (self.month == 10) or (self.month == 12):
                    _l_(14911)

                    if(nd > 31):
                        _l_(14903)

                        cnt = nd - 31
                        _l_(14895)
                        nd = cnt
                        _l_(14896)

                        if(self.month == 12):
                            _l_(14900)

                            self.month = 1
                            _l_(14897)
                            self.year += 1
                            _l_(14898)
                        else:
                            self.month += 1
                            _l_(14899)
                    else:
                        self.day = nd
                        _l_(14901)
                        break
                        _l_(14902)

                elif(self.month == 4) or (self.month == 6) or (self.month == 9) or (self.month == 11):
                    _l_(14910)

                    if(nd > 30):
                        _l_(14909)

                        cnt = nd - 30
                        _l_(14904)
                        nd = cnt
                        _l_(14905)
                        self.month += 1
                        _l_(14906)

                    else:
                        self.day = nd
                        _l_(14907)
                        break
                        _l_(14908)
    ## end of else condition for adaying days
    def formatDate(self,frmt):
        _l_(14927)


        if(frmt == 1):
            _l_(14925)

            ff=str(self.day)+"-"+str(self.month)+"-"+str(self.year)
            _l_(14917)
        elif(frmt == 2):
            _l_(14924)

            ff=str(self.month)+"-"+str(self.day)+"-"+str(self.year)
            _l_(14918)
        elif(frmt == 3):
            _l_(14923)

            ff =str(self.year),"-",str(self.month),"-",str(self.day)
            _l_(14919)
        elif(frmt == 0):
            _l_(14922)

            print("Thanky You.....................")
            _l_(14920)
        else:
            print("Enter Correct Choice.......")
            _l_(14921)
        print(ff)
        _l_(14926)

dt = myDate()
_l_(14929)
nday = int(input("Enter No. For Aday or SUBTRACT Days :: "))
_l_(14930)
dt.adayDays(nday)
_l_(14931)
print("1 : day-month-year")
_l_(14932)
print("2 : month-day-year")
_l_(14933)
print("3 : year-month-day")
_l_(14934)
print("0 : EXIT")
_l_(14935)
frmt = int (input("Enter Your Choice :: "))
_l_(14936)
dt.formatDate(frmt)
_l_(14937)

