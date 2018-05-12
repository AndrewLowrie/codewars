# Your task in order to complete this Kata is to write a function
# which formats a duration, given as a number of seconds, in a
# human-friendly way.
#
# The function must accept a non-negative integer. If it is zero,
# it just returns "now". Otherwise, the duration is expressed as
# a combination of years, days, hours, minutes and seconds.
#
# It is much easier to understand with an example:
#
# format_duration(62)    # returns "1 minute and 2 seconds"
# format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.
#
# Note that spaces are important.
#
# Detailed rules
# The resulting expression is made of components like 4 seconds,
# 1 year, etc. In general, a positive integer and one of the valid
# units of time, separated by a space. The unit of time is used in
# plural if the integer is greater than 1.
#
# The components are separated by a comma and a space (", "). Except
# the last component, which is separated by " and ", just like it
# would be written in English.
#
# A more significant units of time will occur before than a least
# significant one. Therefore, 1 second and 1 year is not correct,
# but 1 year and 1 second is.
#
# Different components have different unit of times. So there is not
#  repeated units like in 5 seconds and 1 second.
#
# A component will not appear at all if its value happens to be zero.
# Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
#
# A unit of time must be used "as much as possible". It means that the
# function should not return 61 seconds, but 1 minute and 1 second instead.
# Formally, the duration specified by of a component must not be greater than
# any valid more significant unit of time.

def format_duration(seconds):

    if seconds == 0:
        return "now"

    results = {
    'second': 0,
    'minute': 0,
    'hour': 0,
    'day': 0,
    'year': 0
    }

    results['second'] = seconds % 60

    minutes = (seconds - results['second']) / 60
    results['minute'] = minutes % 60

    hours = (minutes - results['minute']) / 60
    results['hour'] = hours % 24

    days = (hours - results['hour']) / 24
    results['day'] = days % 365

    years = (days - results['day']) / 365
    results['year'] = years

    answer = []

    if results['year'] > 0:
        if results['year'] > 1:
            answer += [(str(results['year'])) + ' years']
        else:
            answer += [(str(results['year'])) + ' year']

    if results['day'] > 0:
        if results['day'] > 1:
            answer += [(str(results['day'])) + ' days']
        else:
            answer += [(str(results['day'])) + ' day']

    if results['hour'] > 0:
        if results['hour'] > 1:
            answer += [(str(results['hour'])) + ' hours']
        else:
            answer += [(str(results['hour'])) + ' hour']

    if results['minute'] > 0:
        if results['minute'] > 1:
            answer += [(str(results['minute'])) + ' minutes']
        else:
            answer += [(str(results['minute'])) + ' minute']

    if results['second'] > 0:
        if results['second'] > 1:
            answer += [(str(results['second'])) + ' seconds']
        else:
            answer += [(str(results['second'])) + ' second']

    index = 0
    while index < (len(answer)-2):
        answer[index] += ','
        index+=1

    if len(answer) > 1:
        answer[-2] += " and"

    return ' '.join(answer)



print format_duration(1)
# 1 second
print format_duration(62)
# 1 minute and 2 seconds
print format_duration(120)
# 2 minutes
print format_duration(3600)
# 1 hour
print format_duration(3662)
# "1 hour, 1 minute and 2 seconds
