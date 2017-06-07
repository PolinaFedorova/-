s = input('введите строку: ')
s=s+' '
w = 0
min_w = len(s)
for i in s:
    if i != ' ':
            w=w+1
    else:
        if w!=0 and w < min_w:
            min_w=w
            w=0   
	
print('длина самого короткого слова: ', min_w)
