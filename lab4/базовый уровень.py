s=str(input("введите строку:"))
k=0
for i in range(len (s)):
	if s[i]=="*":
		k=i+1
		break
print(k)
