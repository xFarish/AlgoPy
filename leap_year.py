# This function will return a bool
# And takes an int as an input
def leap_year(y: int) -> bool:
    if (y % 4) == 0:
        if (y % 100) == 0:
            if (y % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
