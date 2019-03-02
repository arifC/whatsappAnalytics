import os
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

def calc_avg_msglength(sender, df):
    print("### Calculating avgMsgLength ... ###")
    sum = 0
    count = 0
    for index, msg in df.iterrows():
        if msg['SenderID'] == sender:
            sum += msg['MsgLength']
            count += 1
    avg = sum/count
    print('Average Message Length for sender %s is %s' % (sender, avg))
    return avg

def read_file_with_filter(file):
    print("### Reading chat ... ###")
    script_dir = os.path.dirname(__file__)
    chat_file = "..\\chats\\" + file
    chat_file_dir = os.path.join(script_dir, chat_file)

    lines = []
    for line in open(chat_file_dir, encoding="utf8"):
        if line[0].isdigit() and len(line) >= 20 and ('<Medien ausgeschlossen>' not in line):
            if line[2] == '.':
                lines.append(line.rstrip('\n'))
    print("### Read %s lines from %s" % (len(lines), file))

    temp = []
    #format for this read-out: <DD.MM.YY>, <HH:MM> - <SENDERID>: <MSG>
    for l in lines:
        temp.append({'Date': l[0:8], 'Time': l[10:15], 'SenderID': l[18:19], 'Msg': l[21:], 'MsgLength': len(l[21:])})

    #print(temp)
    df = pd.DataFrame(temp)
    df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%y')
    return df

def main():
    df = read_file_with_filter("chat.txt")
    calc_avg_msglength('A', df)
    calc_avg_msglength('D', df)

if __name__ == "__main__":
    main()