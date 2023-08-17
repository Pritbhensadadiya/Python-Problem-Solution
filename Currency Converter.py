with open('currency.txt') as f:
    lines = f.readlines()
dic = {}
for line in lines:
    curr = line.split("\t")
    dic[curr[0]] = curr[1]

    

print (dic)
# print(dict['Indonesian Rupiah'])100
amount = int(input("Enter the amout to convert::"))
print ("Enter the name of currency you want to convert this amount ? options:\n")

[print(item) for item in dic.keys()]

currency = input ("Enter form given options ")

print (f"{amount }INR is equal to {amount *float( dic[currency])}")
