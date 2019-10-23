import datetime

def time_delta(t1, t2):
    return (int(abs(t1 - t2).total_seconds()))
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
        t2 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')

        print(time_delta(t1, t2))
