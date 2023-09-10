def initialize():
    global recent_owe, interest_owe, cur_day, cur_month, country_history, is_deactivated

    recent_owe = 0
    interest_owe = 0
    cur_day = 1
    cur_month = 1
    country_history = []
    is_deactivated = False

def date_same_or_later(day1, month1, day2, month2):
    if(month1 > month2) or ((month1 == month2) and (day1 >= day2)):
        return True

def all_three_different(c1, c2,c3):
    if(c1 != c2 != c3) and (c1 != c3):
        return True

def purchase(amount, day, month, country):
    global recent_owe, interest_owe, cur_day, cur_month, country_history, is_deactivated

    country_history.append(country)
    if len(country_history) >= 3:
        for c in range(len(country_history)-2):
            if all_three_different(country_history[c],country_history[c+1], country_history[c+2]):
                is_deactivated == True
                return "error"

    if date_same_or_later(day, month, cur_day, cur_month) and (is_deactivated == False):

        update(day, month)
        recent_owe += amount
        cur_day = day
        cur_month = month
        return recent_owe

    else:
        recent_owe == 0
        return "error"

def amount_owed(day, month):
    global recent_owe, interest_owe, cur_day, cur_month, country_history, is_deactivated

    if date_same_or_later(day, month, cur_day, cur_month) and (is_deactivated == False):

        update(day, month)

        cur_day = day
        cur_month = month
        return interest_owe + recent_owe

    else:
        return "error"

def pay_bill(amount, day, month):
    global recent_owe, interest_owe, cur_day, cur_month, country_history, is_deactivated

    if date_same_or_later(day, month, cur_day, cur_month) and (is_deactivated == False):

        update(day, month)

        if interest_owe >= 0:
            if amount >= interest_owe:
                amount -= interest_owe
                interest_owe = 0
                recent_owe -= amount
            else:
                interest_owe -= amount

        cur_day = day
        cur_month = month

    return "error"

def update(day, month):
    global recent_owe, interest_owe, cur_day, cur_month, country_history, is_deactivated

    if (month == cur_month):
        cur_day = day
        cur_month = month
        return interest_owe + recent_owe
    else:
        month_gap = month - cur_month
        interest_owe = interest_owe*(1.05**month_gap)
        interest_owe += recent_owe*(1.05**(month_gap-1))
        recent_owe = 0

initialize()

if __name__ == '__main__':
    initialize()
