
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
    
year = 2024    
leap_year = is_year_leap(year)

print("год " + str(year) + ": " + str(leap_year))