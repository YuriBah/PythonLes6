with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)
    for i in content:
        print(i)

#-----------------------------------------2--------------------------------------------#

import collections

with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    my_dicct = collections.Counter()

    for i in f:
        i = i.split()[0]
        my_dicct[i] += 1

    ip, count = my_dicct.most_common(1)[0][0], my_dicct.most_common(1)[0][1]
    print(f"Spammer {ip} - {count} times")
