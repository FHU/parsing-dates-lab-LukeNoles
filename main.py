from dateutil.parser import parse

def parse_date(user_string):
    dt = parse(user_string)
    return dt.strftime('%m/%d/%Y')


if __name__ == '__main__':
   s = set()
   while True:
        a = input()
        if a != "-1":
            print(parse_date(a))
        if a == "-1":
            break
        else:
            continue
