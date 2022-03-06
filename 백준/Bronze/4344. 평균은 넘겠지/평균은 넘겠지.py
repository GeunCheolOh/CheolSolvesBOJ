def classdata(score):
    N = score[0]
    goodpupil = 0
    avg = (sum(score) - N)/N
    for pupil in range(1, len(score)):
        if score[pupil] > avg:
            goodpupil += 1
    print("{:.3f}%".format((goodpupil/N)*100)) #number expressed rounded to 3 decimal places


C = int(input())
for i in range(C):
    classdata(list(map(int, input().split())))