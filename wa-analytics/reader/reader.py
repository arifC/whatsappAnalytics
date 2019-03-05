import os
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
import analyzer.stats as stats

# This method reads the given file from the chats directory.
#
# Ideas: filter as parameters, make it more generic
def read_file_with_filter(filename):
    print("### Reading chat ... ###")
    script_dir = os.path.dirname(__file__)
    chat_file = "..\\data\\" + filename
    chat_file_dir = os.path.join(script_dir, chat_file)

    lines = []
    for line in open(chat_file_dir, encoding="utf8"):
        if line[0].isdigit() and len(line) >= 20 and ('<Medien ausgeschlossen>' not in line):
            if line[2] == '.':
                lines.append(line.rstrip('\n'))
    print("### Read %s lines from %s" % (len(lines), file))

    temp = []
    #format <DD.MM.YY>, <HH:MM> - <SENDERID>: <MSG>
    for l in lines:
        temp.append({'Date': l[0:8], 'Time': l[10:15], 'SenderID': l[18:19], 'Msg': l[21:], 'MsgLength': len(l[21:])})

    df = pd.DataFrame(temp)
    df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%y')
    return df

def  add_time_dimension_features(df):

    return df

def main():
    df = read_file_with_filter("chat.txt")
    print(df)
    stats.calc_avg_msglength('A', df)
    stats.calc_avg_msglength('D', df)

if __name__ == "__main__":
    main()