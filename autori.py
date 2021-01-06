a = input()
my_list = []
for c in a:
    if c.isupper():
        my_list.append(c)
    else:
        pass
my_list

print(''.join(my_list))