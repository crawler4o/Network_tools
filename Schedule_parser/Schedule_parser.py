import re
from datetime import datetime
from datetime import timedelta

shifts = []
with open('Data\etmTnsMonth.jsp.html') as file:
    for line in file:
        if 'calendarCellRegularFuture' in line:
            date = datetime.strptime(re.search('Details of (.+?)"', line).group(1), '%m/%d/%Y')
            shift = re.search('<span>(.+?)</span>', line).group(1)
            start_date = date.strftime('%m/%d/%Y')
            next_date = date + timedelta(days=1)
            next_date_str = next_date.strftime('%m/%d/%Y')
            if 'STAT' in shift:
                pass
            elif '1900N' in shift:  # night shifts
                shifts.append({'start_date': start_date, 'end_date': next_date_str, 'start_time': '19:00', \
                                                'end_time': '07:00', 'shift': shift, })
            else:
                shifts.append({'start_date': start_date, 'end_date': start_date, 'start_time': '07:00', \
                               'end_time': '19:00', 'shift': shift, })

with open('import_data.csv', 'w') as file:
    file.write('Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private\n')
    for x in shifts:
        file.write(f'{x["shift"]},{x["start_date"]},{x["start_time"]},{x["end_date"]},{x["end_time"]},FALSE,,,FALSE\n')
