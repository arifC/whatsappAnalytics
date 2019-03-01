import os
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

script_dir = os.path.dirname(__file__)
chat_file = os.path.join(script_dir, "..\\chats\\chat.txt")

lines = []
for line in open(chat_file, encoding="utf8"):
    if line[0].isdigit() and len(line) >= 20 and ('<Medien ausgeschlossen>' not in line):
        if line[2] == '.':
            lines.append(line.rstrip('\n'))
print(len(lines))
#pprint(lines)

temp = []
#format for this read-out: <DD.MM.YY>, <HH:MM> - <SENDERID>: <MSG>
for l in lines:
    temp.append({'Date': l[0:8], 'Time': l[10:15], 'SenderID': l[18:19], 'Msg': l[21:], 'MsgLength': len(l[21:])})

#print(temp)
df = pd.DataFrame(temp)
df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%y')
#print(df)

avgMsgLengthA = 0
countA = 0
avgMsgLengthD = 0
countD = 0
for index, msg in df.iterrows():
    if msg['SenderID'] == 'A':
        avgMsgLengthA += msg['MsgLength']
        countA += 1
    else:
        avgMsgLengthD += msg['MsgLength']
        countD += 1

avgMsgLengthA = avgMsgLengthA / countA
print(avgMsgLengthA)

avgMsgLengthD = avgMsgLengthD / countD
print(avgMsgLengthD)