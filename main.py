from dateutil.parser import parse

def parse_date(user_string):
    dt = parse(user_string)
    return dt.strftime('%m/%d/%Y')


if __name__ == '__main__':
    s = []
    while True:
        a = input()
        s.append(a)
        if a == "-1":
            for i in s:
                if i != "-1":
                    print (parse_date(i))
            break
