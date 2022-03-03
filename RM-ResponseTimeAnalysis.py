#Oren Collaco (orenrc@vt.edu)
#Advanced Real-Time Systems 
#Virginia Tech, ECE5550G
# RM Response-Time analysis
#[C, T, D] format 

#Implementation based on lecture notes

Tasks = [[3,7,7], [3,12,12], [5,20,20]]


NoFlag = False
for i in range(0, len(Tasks)):
    C = Tasks[i][0]
    Wsum = 0
    Wsum_t = C
    while(Wsum != Wsum_t):
        Wsum_t = Wsum
        Wsum = 0
        for j in range (0, i+1):
            if(i==j):
                Wsum += C
            else:
                Wsum += Tasks[j][0] * (1 + (int(Wsum_t/Tasks[j][1])))
    if(Wsum <= Tasks[i][2]):
        print("W" + str(int(i+1)) + "=" + str(Wsum) + " <= D=" + str(Tasks[i][2]) + " :)" )
    else:
        print("W" + str(int(i+1)) + "=" + str(Wsum) + " > D=" + str(Tasks[i][2]) + " :(" )
        NoFlag = True
if(NoFlag):
    print("Not RM schedulable")
else:
    print("RM schedulable!")