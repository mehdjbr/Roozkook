
MONTH_DAYS = {1: [0] * 31, 2: [0] * 31, 3: [0] * 31, 4: [0] * 31, 5: [0] * 31, 6: [0] * 31, 7: [0] * 30, 8: [0] * 30,
              9: [0] * 30, 10: [0] * 30, 11: [0] * 30, 12: [0] * 29}


def rest_set(start, length):
    """
    :param start:
    :param length: the time that is needed to finish the task
    :parameter i : counts how many rests we have in one task
    :parameter end: holds the end of task by multiplying i to 15, in this way we add rest times to length
    if we don't have any rest time the end will be equal to the length
    :parameter rest_queue: holds exact time when a rest should start in case to make alarm for rests
    :parameter rest_start: for each student we have specific astane to rest here its 60 minutes so the time between each
    rest is 75 minutes by considering rest_time as 15 minutes
    :return: rest_queue and end
    """
    i = 0
    end = length
    rest_queue = []
    rest_start = 60
    while length > 60:
        length -= 60
        rest_queue[i].append(rest_start)
        i += 1
        rest_start += 75
        end = length + (15*i)
    return rest_queue, end


def school_cross(m, d):
    """
    logic: finds content of index MONTH_DAYS in order to return
    :param m: is month index in MONTH_DAYS
    :param d: is day   index in MONTH_DAYS
    :parameter index: takes what number is located at MONTH_DAYS index
    :return: returns the content of index
    """
    index = MONTH_DAYS[m].index(d - 1)
    if index == 1:
        return 1
    elif index == 3:
        return 3
    elif index == 4:
        return 4


def school_days(m, d):  # set every 7 days off for school days , if the day is already setted to off it give a message that it is off
    """
    logic: in this method we first check if the entered holiday is not already an official day, exam day or relax day
    else it's going to insert the school day as index 2
    :param m: is month index in MONTH_DAYS and ends the
    :param d: is day   index in MONTH_DAYS
    :parameter: off_kind: holds the kind of holiday which there is three kinds: 1-official 2-school 3-relax 4-exam
    :argument school_cross: sets the content to a number
    """
    while (m <= 12):
        for d in range(31):
            off_kind = school_cross(m, d)
            if off_kind is 1:
                print("its already an official offday")
            elif off_kind is 3:
                print("its already a relax day")
            elif off_kind is 4:
                print("its already an exam day")
            else:
                MONTH_DAYS[m].insert(d - 1, 2)
                d += 7
        m += 1


def stu_offday_set(splited_date, seted_reason):
    """
        Logic: it sets the holiday to the calender
        Add the date into holiday dictionary.
        :param splitted_date: holds the 3 variables that user is entered
        :parameter y,m,d takes the three variables that is passed as parameter within splited_date
        :return: persian format of the date
    """
    y, m, d = splitted_date
    if seted_reason == 2:
        school_days(m, d)
    elif seted_reason == 3:
        MONTH_DAYS[m].insert(d - 1, 3)
    elif seted_reason == 4:
        MONTH_DAYS[m].insert(d - 1, 4)


def reason_to_num(reason):
    if reason == 'school':
        return 2
    elif why_off_day == 'relax':
        return 3
    elif why_off_day == 'exam':
        return 4


def offday_check(why_off_day):  # for checking the right reason to set for holiday
    if why_off_day == 'school':
        return 'school'
    elif why_off_day == 'relax':
        return 'relax'
    elif why_off_day == 'exam':
        return 'exam'
    else:
        print("not reasonable!")


def check_date(year, month, day):
    """
    Logic: it checks the correctness of entry month and day
    """
    if year_checker(year) == False:
        raise ValueError("year must be larger than 1300")
    elif month_day_checker(month, day):
        return True
    else:
        raise ValueError("Month or day is wrong.")


def year_checker(year):
    """
    :return: the year should
    """
    return False if year < 1300 or year > 1500 else True


def month_day_checker(month, day):
    if day > 31 or day < 1:
        return False
    elif month > 12 or ((7 <= month) and day == 31) or ((month == 12) and day > 29):
        return False
    else:
        return True


def get_date(holiday_date, split_type='/'):
    """
        get a date from user and split that date into 3 variables like this year, month, day.
        :var: in_range: correctness: it holds the return bool from date_ranger function
        :param holiday_date: it holds the date of holiday that is taken from user
        :param split_type: how to split date.
            for example:: by default 94/1/1 split with '/'
        *NOTE: date must be like these standard formations: 94/1/1 or 94-1-1 or 94|1|1 or etc
        *NOTE FEATURE: must write a function to check is date in a correct format or not.
        :return: a tuple with split days.
    """
    import re
    if split_type == '/':
        pattern = r'^\d{4}\/\d{2}\/\d{2}$'
    else:
        pattern = r'^\d{4}' + split_type + r'\d{2}' + split_type + r'\d{2}$'
    if re.search(pattern, holiday_date):
        if split_type in holiday_date:
            year, month, day = [int(str(x)) for x in holiday_date.split(split_type)]
        else:
            raise ValueError("split the date with {}".format(split_type))
    else:
        raise ValueError("Please Enter true format of date. The format is: {}".format('xxxx' + split_type + 'xx' + split_type + 'xx'))
    if type(year) != int or type(month) != int or type(day) != int:
        raise ValueError("please correct your date")
    if check_date(year, month, day):
        return year, month, day


def convert_to_jalali(jalali_date, format='%A %D %B %N'):
    """
        gets input from get_date function
        :param jalali_date: splits the date to 3 variables y=year,m=month,d=day.
        :param format: the way to show date in jalali
        :return: persian format of the date
    """
    from khayyam import JalaliDate
    if check_dependencies():
        from khayyam import JalaliDate
    y, m, d = jalali_date
    return JalaliDate(year=y, month=m, day=d).strftime(format)


def add_to_holiday(splitted_date):
    """
        Logic: it sets the holiday to the calender
        Add the date into holiday dictionary.
        :param splitted_date: holds the 3 variables that user is entered
        :var y, m, d takes the three variables that is passed as parameter within splited_date
        *NOTE FEATURE: Check inner comment
        :return: persian format of the date
    """
    y, m, d = splitted_date
    MONTH_DAYS[m].insert(d - 1, 1)
    check_add(m, d)


def check_add(m, d):
    """
    this method is for official holidays
    :return: if it is set to dict return True else return false
    """
    return True if MONTH_DAYS[m][d-1] == 1 else False


def check_dependencies():
    """
    :var: package_name: gets the name of a package that we want to check its existence
    function: find_module:: Finds the loader for a module
    :var: spec_find:  If a spec of module cannot be found, None is returned
    :if: true: it checks if the modules has been found or not
    """
    import importlib.util
    package_name = 'khayyam'
    spec_find = importlib.util.find_spec(package_name)
    if spec_find is None:
        raise ImportError(package_name + " is not installed")
    else:
        return True


def menu(select_menu):
    """
    :var select_menu : the menu number that is taken from user
    :return the select_menu as numbers 1:add official holiday 2:student calender 3:set student task
    4:global calender 5:help!
    :raise a ValueError for wrong inputs
    """
    if select_menu == '1':
        return 1
    elif select_menu == '2':
        return 2
    elif select_menu == '3':
        return 3
    elif select_menu == '4':
        return 4
    elif select_menu == '5':
        return 5
    else:
        raise ValueError("wrong command!")


print("Welcome to version 0.3.0 please select your option (only one number)")

select_menu = input("""
please select your task
1- add official holiday
2- student calender
3- set student task
4- global calender
5- help!
""")

int_menu = menu(select_menu)

if int_menu == 1:
    holiday_date = input("enter holiday date to set\n")
    splitted_date = get_date(holiday_date)
    print(splitted_date)
    add_to_holiday(splitted_date)
    jalali_date = splitted_date
    print(MONTH_DAYS)


elif int_menu == 2:
    holiday_date = input("enter holiday date to set\n")
    splitted_date = get_date(holiday_date)
    why_off_day = input("why you are off in this day?!\n")
    reason = offday_check(why_off_day)
    seted_reason = reason_to_num(reason)
    stu_offday_set(splitted_date, seted_reason)
    print(MONTH_DAYS)


elif int_menu == 3:
    rest_time = 15
    date = input("enter your date \n")
    task = input("what is your task?! \n")
    start = input("when do you plan to do it?! \n")
    length = input("how much time do you need?! please enter by minutes \n")
    rest_queue, end = rest_set(length, start)
    print("your task starts at{} \n".format(start))
    print("your task ends at {} \n".format(end))
    print("your start rests are at these times {}".format(rest_queue))


elif int_menu == 4:
    print(MONTH_DAYS)

elif int_menu == 5:
    print("Shelom")


