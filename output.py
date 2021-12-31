from sessions import Sessions, TIMES_OF_DAY, DAYS_WEEK
import pandas as pd


def create_output_file(output=None):
    df = pd.DataFrame(columns=TIMES_OF_DAY, index=DAYS_WEEK)

    for i in Sessions.all:
        df.at[i.day, i.time] = i.assignee

    if output is None:
        print(df)
    else:
        df.to_excel(excel_writer='Rota.xlsx')
        print(df)
