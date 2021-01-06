rows, columns, new_rows, new_columns = map(int, input().split())

for i in range(rows):
  line = list(input())
  c = ("".join([x * new_columns for x in line]))
  for i in range(new_rows):
    print(c)