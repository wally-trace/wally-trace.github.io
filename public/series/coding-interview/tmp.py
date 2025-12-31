import sys
import re

f = open(sys.argv[1], 'r')
m, s = 0, 0
p = r'\([^:)]*:[^:)]*\)'
lines = f.readlines()
for l in lines:
	if re.search(p, l):
		print(l)
		l = l.split('(')[1]
		m += int(l.split(':')[0])
		s += int(l.split(':')[1].split(')')[0])

h = 0
added_m, s = divmod(s, 60)
m += added_m

added_h, m = divmod(m, 60)
h += added_h

print(f"{h:02}:{m:02}:{s:02}")
