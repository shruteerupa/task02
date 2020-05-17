sample={'physics':88,'maths':75,'chemistry':72,'basic electrical':89}

print("The original dictionary is : " + str(sample))
temp = min(sample.values())
res = [key for key in sample if sample[key] == temp]
print("Keys with minimum values are : " + str(res)) 