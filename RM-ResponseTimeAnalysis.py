#Oren Collaco (orenrc@vt.edu)
#Advanced Real-Time Systems 
#Virginia Tech, ECE5550G
# RM Response-Time analysis
#[C, T, D] format 

#Implementation based on lecture notes


#IMPORTANT! Tasks should be ordered with highest priority first
Tasks = [[5,20,15], [10,40,30], [20,50,40]]

NoFlag = False
for i in range(0, len(Tasks)):
    C = Tasks[i][0]
    Wsum = 0
    Wsum_t = C
    while(Wsum != Wsum_t and Wsum <= Tasks[i][2]):
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
  print("Not schedulable based on response-time analysis")
else:
    print("Schedulable based on response-time analysis!")

