def check_int_date(date):
    check = ''
    result = ''
    lst = []
    for i in date:
        check = i.isdigit()
        lst.append(check)
    if lst[0] == True and lst[1] == True and lst[2] == True:
        result = True
        return result
    else:
        result = False
        return result
