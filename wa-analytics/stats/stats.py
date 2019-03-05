import sys

# This method calculates the average message length for a particular sender.
#
# Ideas: -
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