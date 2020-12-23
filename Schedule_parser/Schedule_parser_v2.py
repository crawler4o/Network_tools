import pandas as pd
from datetime import datetime
from datetime import timedelta


def parse_the_file(html_file):

    output_schedule = []

    with open(html_file, 'r') as file:
        df = pd.read_html(file, match='WORK')
    df = df[1:]

    for x in df:
        shift = x.iloc[0, 1]
        date = x.iloc[0, 0]

        if '700' in shift:
            shift = shift[:10]
        elif '1900' in shift:
            shift = shift[:11]
        else:
            shift = 'ERROR'

        output_schedule.append([date, shift])

    return output_schedule


def prep_the_data(workbrain_nfo, monthy):

    shifts = []

    for x in workbrain_nfo:
        start_date = f"{monthy}/{x[0]}/{year}"
        date = datetime.strptime(start_date, '%m/%d/%Y')
        next_day = date + timedelta(days=1)
        next_day_str = next_day.strftime('%m/%d/%Y')

        if '700' in x[1]:
            shift = f"D_{x[1][-3:]}"
            end_date = start_date
            end_time = '19:00'
            start_time = '07:00'
        elif '1900' in x[1]:
            shift = f"N_{x[1][-3:]}"
            end_date = next_day_str
            end_time = '07:00'
            start_time = '19:00'
        else:
            shift = 'ERROR'
            end_date = 'ERROR'
            end_time = 'ERROR'
            start_time = 'ERROR'

        shifts.append({'start_date': start_date, 'end_date': end_date, 'start_time': start_time, 'end_time': end_time,
                       'shift': shift})

    return shifts


def writer(shifts):
    with open('import_data.csv', 'w') as file:
        file.write('Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private\n')
        for x in shifts:
            file.write(
                f'{x["shift"]},{x["start_date"]},{x["start_time"]},{x["end_date"]},{x["end_time"]},FALSE,,,FALSE\n')


def user_month():

    monthr = input('Enter month please in MM format. Like August is 08: ')

    try:
        if int(monthr) in range(1, 13):
            return monthr
        else:
            exit()
    except:
        print('Bad entry. Try again.')
        exit()


if __name__ == '__main__':

    source_file = 'WORKBRAIN - Employee Self Service Kiosk.html'
    year = '2021'

    month = user_month()
    workbrain = parse_the_file(source_file)
    clean_data = prep_the_data(workbrain, month)
    writer(clean_data)

