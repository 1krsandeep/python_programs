import datetime
y = input('What\'s your date of birth(in yyyy-mm-dd format)')
print(y)
x = datetime.datetime.now()
print(x)
py = int(x.strftime('%Y')) #present year
pm = int(x.strftime('%m')) #present month
pd = int(x.strftime('%d')) #present date

by = int(y[0:4]) #birth year
bm = int(y[5:7]) #birth month
bd = int(y[8:10]) #birth date
if pm > bm:
    year = py - by
    m = pm - bm
elif pm < bm:
    year = py - by -1
    m = 12 - (bm - pm)
else:
    if pd < bd:
        year = py - by - 1
        m = 11
    else:
        year = py - by
        m = 0

#leap year check
if py % 100 == 0 and py % 400 == 0:
    dpy = 1
elif py % 100 == 0 and py % 400 != 0:
    dpy = 0
elif py % 4 == 0:
    dpy = 1
else:
    dpy = 0

#to count the number of days
if pm == 5 or pm == 7 or pm == 10 or pm == 12:
    d1 = 30
elif pm == 1 or pm == 2 or pm == 4 or pm == 6 or pm == 8 or pm == 9 or pm == 11:
    d1 = 31
else:
    if dpy == 1:
        d1 = 29
    else:
        d1 = 28

if pd > bd:
    d = pd - bd
elif pd < bd:
    d = d1 - (bd - pd)
else:
    d = 0

print(f'You are {year} years {m} months and {d} days old')
