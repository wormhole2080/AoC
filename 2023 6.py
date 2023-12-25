import numpy as np
def distance_covered(wait, length):
    return (length - wait) * wait

def findMyOptions(durations, distance_to_beat):
    for i in range(len(durations)):
        options = []
        options = [int(a) for a in list(range(1,durations[i]+1)) if distance_covered(a, durations[i]) > distance_to_beat[i] ]
    return options

if __name__ == "__main__":
    durations = [41,66,72,66]
    distance_to_beat =[244,1047,1228,1040]
    numOptions=[]
    numOptions.append(len(findMyOptions(durations, distance_to_beat)))
    #
    print (np.prod(numOptions))

    durations = [41667266]
    distance_to_beat =[244104712281040]
    numOptions=[]
    numOptions.append(len(findMyOptions(durations, distance_to_beat)))
    print (np.prod(numOptions))
