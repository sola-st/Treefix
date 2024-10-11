# Extracted from https://stackoverflow.com/questions/6470428/catch-multiple-exceptions-in-one-line-except-block
#This example code is a technique I use in a library that connects with websites to gather data

ConnectErrs  = (URLError, SSLError, SocketTimeoutError, BadStatusLine, ConnectionResetError)

def connect(url, data):
    #do connection and return some data
    return(received_data)

def some_function(var_a, var_b, ...):
    try: o = connect(url, data)
    except ConnectErrs as e:
        #do the recovery stuff
    blah #do normal stuff you would do if no exception occurred

