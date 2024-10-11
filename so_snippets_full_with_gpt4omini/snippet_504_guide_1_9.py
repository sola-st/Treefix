input = lambda prompt: '31' if 'day' in prompt else '5' if 'Month' in prompt else '2023' if 'Year' in prompt else '10' # pragma: no cover
print = lambda x: None # pragma: no cover
nday = 5 # pragma: no cover
frmt = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6871016/adding-days-to-a-date-in-python
from l3.Runtime import _l_
class myDate:
    _l_(3165)


    def __init__(self):
        _l_(3078)

        self.day = 0
        _l_(3057)
        self.month = 0
        _l_(3058)
        self.year = 0
        _l_(3059)
        ## for checking valid days month and year
        while (True):
            _l_(3065)

            d = int(input("Enter The day :- "))
            _l_(3060)
            if (d > 31):
                _l_(3064)

                print("Plz 1 To 30 value Enter ........")
                _l_(3061)
            else:
                self.day = d
                _l_(3062)
                break
                _l_(3063)

        while (True):
            _l_(3071)

            m = int(input("Enter The Month :- "))
            _l_(3066)
            if (m > 13):
                _l_(3070)

                print("Plz 1 To 12 value Enter ........")
                _l_(3067)
            else:
                self.month = m
                _l_(3068)
                break
                _l_(3069)

        while (True):
            _l_(3077)

            y = int(input("Enter The Year :- "))
            _l_(3072)
            if (y > 9999 and y < 0000):
                _l_(3076)

                print("Plz 0000 To 9999 value Enter ........")
                _l_(3073)
            else:
                self.year = y
                _l_(3074)
                break
                _l_(3075)
    ## method for aday ands cnttract days
    def adayDays(self, n):
        _l_(3153)

        ## aday days to date day
        nd = self.day + n
        _l_(3079)
        print(nd)
        _l_(3080)
        ## check days subtract from date
        if nd == 0:
            _l_(3152)

            if(self.year % 4 == 0):
                _l_(3089)

                if(self.month == 3):
                    _l_(3084)

                    self.day = 29
                    _l_(3081)
                    self.month -= 1
                    _l_(3082)
                    self.year = self. year
                    _l_(3083)
            else:
                if(self.month == 3):
                    _l_(3088)

                    self.day = 28
                    _l_(3085)
                    self.month -= 1
                    _l_(3086)
                    self.year = self. year
                    _l_(3087)
            if  (self.month == 5) or (self.month == 7) or (self.month == 8) or (self.month == 10) or (self.month == 12):
                _l_(3100)

                self.day = 30
                _l_(3090)
                self.month -= 1
                _l_(3091)
                self.year = self. year
                _l_(3092)
            elif (self.month == 2) or (self.month == 4) or (self.month == 6) or (self.month == 9) or (self.month == 11):
                _l_(3099)

                self.day = 31
                _l_(3093)
                self.month -= 1
                _l_(3094)
                self.year = self. year
                _l_(3095)

            elif(self.month == 1):
                _l_(3098)

                self.month = 12
                _l_(3096)
                self.year -= 1    
                _l_(3097)    
        ## nd == 0 if condition over
        ## after subtract days to day io goes into negative then
        elif nd < 0 :
            _l_(3151)

            n = abs(n)## return positive if no is negative
            _l_(3101)## return positive if no is negative
            for i in range (n,0,-1):
                _l_(3117)

                
                if self.day == 0:
                    _l_(3116)


                    if self.month == 1:
                        _l_(3114)

                        self.day = 30
                        _l_(3102)
                        
                        self.month = 12
                        _l_(3103)
                        self.year -= 1
                        _l_(3104)
                    else:
                        self.month -= 1
                        _l_(3105)
                        if(self.month == 1) or (self.month == 3)or (self.month == 5) or (self.month == 7) or (self.month == 8) or (self.month == 10) or (self.month ==12):
                            _l_(3113)

                            self.day = 30
                            _l_(3106)
                        elif(self.month == 4)or (self.month == 6) or (self.month == 9) or (self.month == 11):
                            _l_(3112)

                            self.day = 29
                            _l_(3107)
                        elif(self.month == 2):
                            _l_(3111)

                            if(self.year % 4 == 0):
                                _l_(3110)

                                self.day == 28
                                _l_(3108)
                            else:
                                self.day == 27
                                _l_(3109)
                else:
                    self.day -= 1
                    _l_(3115)

        ## enf of elif negative days
        ## adaying days to DATE
        else:
            cnt = 0
            _l_(3118)
            while (True):
                _l_(3150)


                if self.month == 2:
                    _l_(3149)

                    
                    if(self.year % 4 == 0):
                        _l_(3131)

                        if(nd > 29):
                            _l_(3124)

                            cnt = nd - 29
                            _l_(3119)
                            nd = cnt
                            _l_(3120)
                            self.month += 1
                            _l_(3121)
                        else:
                            self.day = nd
                            _l_(3122)
                            break
                            _l_(3123)
                ## if not leap year then
                    else:  
                    
                        if(nd > 28):
                            _l_(3130)

                            cnt = nd - 28
                            _l_(3125)
                            nd = cnt
                            _l_(3126)
                            self.month += 1
                            _l_(3127)
                        else:
                            self.day = nd
                            _l_(3128)
                            break
                            _l_(3129)
                ## checking month other than february month
                elif(self.month == 1) or (self.month == 3) or (self.month == 5) or (self.month == 7) or (self.month == 8) or (self.month == 10) or (self.month == 12):
                    _l_(3148)

                    if(nd > 31):
                        _l_(3140)

                        cnt = nd - 31
                        _l_(3132)
                        nd = cnt
                        _l_(3133)

                        if(self.month == 12):
                            _l_(3137)

                            self.month = 1
                            _l_(3134)
                            self.year += 1
                            _l_(3135)
                        else:
                            self.month += 1
                            _l_(3136)
                    else:
                        self.day = nd
                        _l_(3138)
                        break
                        _l_(3139)

                elif(self.month == 4) or (self.month == 6) or (self.month == 9) or (self.month == 11):
                    _l_(3147)

                    if(nd > 30):
                        _l_(3146)

                        cnt = nd - 30
                        _l_(3141)
                        nd = cnt
                        _l_(3142)
                        self.month += 1
                        _l_(3143)

                    else:
                        self.day = nd
                        _l_(3144)
                        break
                        _l_(3145)
    ## end of else condition for adaying days
    def formatDate(self,frmt):
        _l_(3164)


        if(frmt == 1):
            _l_(3162)

            ff=str(self.day)+"-"+str(self.month)+"-"+str(self.year)
            _l_(3154)
        elif(frmt == 2):
            _l_(3161)

            ff=str(self.month)+"-"+str(self.day)+"-"+str(self.year)
            _l_(3155)
        elif(frmt == 3):
            _l_(3160)

            ff =str(self.year),"-",str(self.month),"-",str(self.day)
            _l_(3156)
        elif(frmt == 0):
            _l_(3159)

            print("Thanky You.....................")
            _l_(3157)
        else:
            print("Enter Correct Choice.......")
            _l_(3158)
        print(ff)
        _l_(3163)

dt = myDate()
_l_(3166)
nday = int(input("Enter No. For Aday or SUBTRACT Days :: "))
_l_(3167)
dt.adayDays(nday)
_l_(3168)
print("1 : day-month-year")
_l_(3169)
print("2 : month-day-year")
_l_(3170)
print("3 : year-month-day")
_l_(3171)
print("0 : EXIT")
_l_(3172)
frmt = int (input("Enter Your Choice :: "))
_l_(3173)
dt.formatDate(frmt)
_l_(3174)

