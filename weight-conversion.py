answer = input("Would you like to convert to pounds or kilograms: ")

if answer == 'pounds':
    pounds_var = input('Enter weight in kilograms: ')
    lbs_to_kg = int(pounds_var)*2.2046
    print(str(lbs_to_kg) + "kg")
elif answer == 'kilo' or 'kilograms' or 'kilos':
    kilo_var = input('Enter weight in pounds: ')
    kg_to_lbs = int(kilo_var)/2.2046
    print(str(kg_to_lbs) + 'lbs')