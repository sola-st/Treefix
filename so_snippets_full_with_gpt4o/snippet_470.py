# Extracted from https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters
class MyClass:
    def __init__(self, attrvalue):
        self.myattr = attrvalue
    def __getattribute__(self, attr):
        if attr == "myattr":
            #Getter for myattr
    def __setattr__(self, attr):
        if attr == "myattr":
            #Setter for myattr

