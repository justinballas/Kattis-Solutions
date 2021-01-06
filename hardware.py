def find_all_digits(start, end, interval):
    arr = [start]
    counter = start
    for i in range(int((end - start) / interval)):
        counter += interval
        arr.append(counter)
    return arr


def list_to_str(arr):
    string_ints = [str(int) for int in arr]
    str_of_ints = "".join(string_ints)
    return (str_of_ints)


def freq_digits(digit_list):
    freq = {}
    for i in digit_list:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    return freq


n = int(input())

for i in range(n):
    street_name = input()
    num_addresses, word = input().split()
    num_addresses = int(num_addresses)
    all_digits = ''
    counter = 0
    while counter < num_addresses:
        x = input().split()
        if x[0] == '+':
            start = x[1]
            end = x[2]
            interval = x[3]
            dig_list = find_all_digits(int(start), int(end), int(interval))
            all_digits += list_to_str(dig_list)
            counter += len(dig_list)
        else:
            all_digits += str(x[0])
            counter += 1

    digits_freq = freq_digits(all_digits)

    print(street_name)
    print(num_addresses, word)

    for i in range(0, 9 + 1):
        if '{}'.format(i) not in digits_freq.keys():
            print('make 0 digit {}'.format(i))
        else:
            print('make {} digit {}'.format(digits_freq['{}'.format(i)], i))
    if len(all_digits) == 1:
        print('In total 1 digit')
    else:
        print('In total {} digits'.format(len(all_digits)))
