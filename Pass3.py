from sys import argv

with open('bakery.csv.txt', 'a', encoding='utf-8') as donut_a:
    with open('bakery.csv.txt', 'r', encoding='utf-8') as donut_r:
        if len(argv) > 1 and [i for i in argv[1:] if i.replace('.', '').isdigit()]:
            if len(argv) == 3:
                print(*donut_r.read().split()[int(argv[1]) - 1:int(argv[2])], sep='\n')
            if ',' in argv[1] or '.' in argv[1]:
                donut_r.read()
                print(argv[1], file=donut_a)
            else:
                print(*donut_r.readlines()[int(argv[1]) - 1:], sep='')
        else:
            print(donut_r.read())

