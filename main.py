from datetime import datetime

def parse_date(user_string):
    dt = user_string.replace(",", '')
    split = dt.split()
    for i in split:
        i.lstrip("0")
    tupl = tuple(split)
    unsplit =" ".join(tupl)
    return datetime.strptime(unsplit, '%B %d %Y').strftime('%m/%d/%Y')


if __name__ == '__main__':
    s = []
    while True:
        a = input()
        s.append(a)
        if a == "-1":
            for i in s:
                if i != "-1":
                    print (parse_date(i))
                else:
                    break
            break
