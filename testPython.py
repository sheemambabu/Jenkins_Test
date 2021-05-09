import os

print(os.getcwd())

f = open("Testing_1.txt","a")
for i in range(10):
  f.write("This is line %d\r\n" % (i+1))

f.close()
