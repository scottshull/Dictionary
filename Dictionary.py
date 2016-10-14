holiday = dict(0)
print holiday

holiday = {'Halloween': 'October 31', 'Thanksgiving': 'November 24', 'Christmas': 'December 25', 'New Year Eve': ' December 31', 'New Year Day': 'January 1',}
print holiday

len(holiday)
print (len(holiday))

if 'Halloween' in holiday:
    print "True"
else:
    print "False"

if 'Thanksgiving' in holiday:
    print "True"
else:
    print "False"

vals = holiday.values()
'Christmas' in vals
print vals

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def print_hist(h):
    for a in h:
        print a, h[a]
        
