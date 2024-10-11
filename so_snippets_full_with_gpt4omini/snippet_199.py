# Extracted from https://stackoverflow.com/questions/441147/how-to-subtract-a-day-from-a-date
class myDate:

    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0
        ## for checking valid days month and year
        while (True):
            d = int(input("Enter The day :- "))
            if (d > 31):
                print("Plz 1 To 30 value Enter ........")
            else:
                self.day = d
                break

        while (True):
            m = int(input("Enter The Month :- "))
            if (m > 13):
                print("Plz 1 To 12 value Enter ........")
            else:
                self.month = m
                break

        while (True):
            y = int(input("Enter The Year :- "))
            if (y > 9999 and y < 0000):
                print("Plz 0000 To 9999 value Enter ........")
            else:
                self.year = y
                break
    ## method for aday ands cnttract days
    def adayDays(self, n):
        ## aday days to date day
        nd = self.day + n
        print(nd)
        ## check days subtract from date
        if nd == 0: ## check if days are 7  subtracted from 7 then,........
            if(self.year % 4 == 0):
                if(self.month == 3):
                    self.day = 29
                    self.month -= 1
                    self.year = self. year
            else:
                if(self.month == 3):
                    self.day = 28
                    self.month -= 1
                    self.year = self. year
            if  (self.month == 5) or (self.month == 7) or (self.month == 8) or (self.month == 10) or (self.month == 12):
                self.day = 30
                self.month -= 1
                self.year = self. year
                   
            elif (self.month == 2) or (self.month == 4) or (self.month == 6) or (self.month == 9) or (self.month == 11):
                self.day = 31
                self.month -= 1
                self.year = self. year

            elif(self.month == 1):
                self.month = 12
                self.year -= 1    
        ## nd == 0 if condition over
        ## after subtract days to day io goes into negative then
        elif nd < 0 :   
            n = abs(n)## return positive if no is negative
            for i in range (n,0,-1): ## 
                
                if self.day == 0:

                    if self.month == 1:
                        self.day = 30
                        
                        self.month = 12
                        self.year -= 1
                    else:
                        self.month -= 1
                        if(self.month == 1) or (self.month == 3)or (self.month == 5) or (self.month == 7) or (self.month == 8) or (self.month == 10) or (self.month ==12):
                            self.day = 30
                        elif(self.month == 4)or (self.month == 6) or (self.month == 9) or (self.month == 11):
                            self.day = 29
                        elif(self.month == 2):
                            if(self.year % 4 == 0):
                                self.day == 28
                            else:
                                self.day == 27
                else:
                    self.day -= 1

        ## enf of elif negative days
        ## adaying days to DATE
        else:
            cnt = 0
            while (True):

                if self.month == 2:  # check leap year
                    
                    if(self.year % 4 == 0):
                        if(nd > 29):
                            cnt = nd - 29
                            nd = cnt
                            self.month += 1
                        else:
                            self.day = nd
                            break
                ## if not leap year then
                    else:  
                    
                        if(nd > 28):
                            cnt = nd - 28
                            nd = cnt
                            self.month += 1
                        else:
                            self.day = nd
                            break
                ## checking month other than february month
                elif(self.month == 1) or (self.month == 3) or (self.month == 5) or (self.month == 7) or (self.month == 8) or (self.month == 10) or (self.month == 12):
                    if(nd > 31):
                        cnt = nd - 31
                        nd = cnt

                        if(self.month == 12):
                            self.month = 1
                            self.year += 1
                        else:
                            self.month += 1
                    else:
                        self.day = nd
                        break

                elif(self.month == 4) or (self.month == 6) or (self.month == 9) or (self.month == 11):
                    if(nd > 30):
                        cnt = nd - 30
                        nd = cnt
                        self.month += 1

                    else:
                        self.day = nd
                        break
                ## end of month condition
        ## end of while loop
    ## end of else condition for adaying days
    def formatDate(self,frmt):

        if(frmt == 1):
            ff=str(self.day)+"-"+str(self.month)+"-"+str(self.year)
        elif(frmt == 2):
            ff=str(self.month)+"-"+str(self.day)+"-"+str(self.year)
        elif(frmt == 3):
            ff =str(self.year),"-",str(self.month),"-",str(self.day)
        elif(frmt == 0):
            print("Thanky You.....................")
            
        else:
            print("Enter Correct Choice.......")
        print(ff)
            
            

dt = myDate()
nday = int(input("Enter No. For Aday or SUBTRACT Days :: "))
dt.adayDays(nday)
print("1 : day-month-year")
print("2 : month-day-year")
print("3 : year-month-day")
print("0 : EXIT")
frmt = int (input("Enter Your Choice :: "))
dt.formatDate(frmt)

    enter code here

