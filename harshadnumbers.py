num = input()

num_list = list(map(int, num))

int_num = int(num)

if int_num % sum(num_list) == 0:
  print(num)
else:
  while int_num % sum(num_list) != 0:
    int_num += 1
    num_list = list(map(int, str(int_num)))
    if int_num % sum(num_list) == 0:
      print(int_num)