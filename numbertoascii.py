print "Check ASCII value"
print "1. Number to ASCII Value"
print "2. ASCII to Number value"
inp1 = str(raw_input("Enter your choice : "))

if inp1 == "1":
    num = int(raw_input("Enter number to check ASCII Value : "))
    print "ASCII Value for ",num,"is ",chr(num)
else:
    asci = str(raw_input("Enter ASCII value to check number : "))
    print " number is ",ord(asci), "For ASCII Value ",asci
    
