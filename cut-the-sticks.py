def cut_sticks(n,s):

        for _ in range(n):
            if len(s) > 0:
                print len(s)
                s = [x - min(s) for x in s if x - min(s) > 0]

num = int(raw_input().strip())

sticks = [int(i) for i in raw_input().strip().split()]

cut_sticks(num,sticks)
