# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import re
with open('model.dat', 'r') as f:
    data = f.read()
found = re.findall(r'=', data, re.M | re.S)
pattern='='

spt=re.split(pattern, data)
print(len(spt))
print(len(spt))
#(key, value) = data.split()

print (spt[1])
print (spt[7])

a_dictionary = {}
a_file = open("model.dat")


#for line in a_file:
#    print(line)
#    (key, val) = line.split('=')
#   a_dictionary[key] = val

#print(a_dictionary)

d = dict(f.split("=") for f in str.split(" "))

for k, v in d.items():
    print(k, v)


#for founds in found:
#    print(founds)

s = ":dfa:sif:e"
print(s[1:])

with open('model.dat', 'r') as f:
    data = f.read()

gg = open('new_model.txt', 'w')

#lines = f.readlines()
for line in data:
     gg.write(line)
 #    gg.write(line[1:])

for line in data:
    print(line)

"""with open("demo-out.txt","w") as output:
    with open("model.dat","r") as input:
        data=input.read()
        data = data.replace("+", "")
        output.write(data)"""







#with open("demo-out.txt","w") as output:
#   with open("model.dat","r") as input:
#       for line in input:
#          output.write(input.read()[1:])


#with open("model.dat","w") as modl:

