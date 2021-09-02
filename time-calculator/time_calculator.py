def add_time(start, duration, day=None):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    startMinutes = 0

    midday = start[-2:]
    start = start[:-2].split(':')
    if midday == 'AM':
      if start[0] != '12':
        startMinutes += int(start[0]) * 60
      startMinutes += int(start[1])
    else:
      if (start[0] != '12'):
        startMinutes += 12 * 60
      startMinutes += int(start[0]) * 60 + int(start[1])

    duration = duration.split(':')
    durationMinutes = int(duration[0]) * 60 + int(duration[1])
    newMinutes = startMinutes + durationMinutes

    newMins = newMinutes % 60
    newHours = newMinutes // 60 % 24
    newDays = newMinutes // 60 // 24
    flag = ''
    new_time = ''

    if newHours == 0:
      flag = 'AM'
      newHours = 12
    elif newHours < 12:
      flag = 'AM'
    elif newHours == 12:
      flag = 'PM'
      newHours = 12
    else:
      flag = 'PM'
      newHours -= 12

    new_time = str(newHours) + ":" + str(newMins).zfill(2) + ' ' + flag


    if day:
      day = day[0].upper() + day[1:].lower()
      dayNum = (days.index(day) + newDays) % 7
      new_time += ', ' + days[dayNum]

    if (newDays == 1):
      new_time += ' (next day)'
    elif (newDays > 1):
      new_time += ' (' + str(newDays) + ' days later)'

    return new_time