s = input()

first = s.find('f')
last_rev = s[::-1].find('f')

last = len(s)-1-last_rev if last_rev != -1 else -1

if first != last:
    print(first, last)
elif first != -1:
    print(first)
