Patrons = input('Patrons?')
if Patrons == 'full':
    waitEstimate = float(input('waitEstimate?'))
    if 10 < waitEstimate <= 30:
        Hungry = input('Hungry?')
        if Hungry == 'Yes':
            Alternate = input('Alternate?')
            if Alternate == 'yes':
                Raning = input('Raining?')
                if Raning == 'yes':
                    print('yes')
                elif Raning == 'no':
                    print('no')
                else:
                    print('wrong entry')
            elif Alternate == 'no':
                print('yes')
            else:
                print('wrong entry')
        elif Hungry == 'No':
            print('yes')
        else:
            print('wrong entry')
    elif 30 < waitEstimate <= 60:
        Alternate = input('Alternate?')
        if Alternate == 'yes':
            Fri_sat = input('Fri/sat?')
            if Fri_sat == 'yes':
                print('Yes')
            elif Fri_sat == 'no':
                print('no')
        elif Alternate == 'no':
            Reservation = input('Reservation?')
            if Reservation == 'yes':
                print('Yes')
            elif Reservation == 'no':
                Bar = input('Bar?')
                if Bar == 'yes':
                    print('Yes')
                elif Bar == 'no':
                    print('No')
                else:
                    print('wrong entry')
            else:
                print('wrong entry')
        else:
            print('wrong entry')
    elif 60 < waitEstimate:
        print('no')
    else:
        print('wrong entry')
elif Patrons == 'some':
    print('yes')
elif Patrons == 'none':
    print('no')
else:
    print('wrong entry')   



