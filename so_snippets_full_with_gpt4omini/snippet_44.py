# Extracted from https://stackoverflow.com/questions/466345/convert-string-jun-1-2005-133pm-into-datetime
#Convert String to datetime
x=datetime.strptime('Jun 1 2005', '%b %d %Y').date()
print(x,type(x))
2005-06-01 00:00:00 <class 'datetime.datetime'>


#Convert datetime to String (Reverse above process)
y=x.strftime('%b %d %Y')
print(y,type(y))
Jun 01 2005 <class 'str'>

