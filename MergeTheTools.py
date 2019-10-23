def merge_the_tools(string, k):
    string = [string[i:i+k] for i in range(0, len(string), k)]
    for i in string:
        s = ''
        for j in i:
            if j not in s:
                s=s+j
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
