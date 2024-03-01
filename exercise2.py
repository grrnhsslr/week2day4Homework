# 2) Best Time to Meet
# Billy is trying to figure out if there is a time that he and his team can meet to work on the project.
# His three teammates each give him a set of times they are available ('HH:MM' 24-hour).
# Create a function that will take in any number of sets of available times (remember *args)
# and return a set of times when everyone can meet.

person1 = {'09:00', '10:30', '11:30', '12:00', '13:00', '14:30'}
person2 = {'09:30', '10:00', '10:30', '12:00', '14:30', '16:00'}
person3 = {'09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00'}
person4 = {'11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00'}
person5 = {'14:30'}
def number(persons):
    returnset = persons[0]  # uses person1 as 'billy' to compare his available times to the rest of his teams times
    for person in persons:  # for each person in the team it checks their times
        returnset = returnset.intersection(person)  # use an intersection to see if the times are available for everyone
    return returnset  # returns the available times

print(number([person1, person2, person3, person4, person5]))  # shows all available times that the team has in common
