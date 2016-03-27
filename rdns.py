f = open('3.2.1.db', 'a')
for x in range(1,256):
  s = "%d\tPTR\tstatic.dtbnet.com.\n" % (x)
  f.write(s)
