def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    temp = []
    inactive = 0
    active = 1
    for i in range(days):
        del temp
        temp = []
        for i in range(len(states)):
            if i == 0:
                if states[i+1] == inactive:
                    temp.append(inactive)
                if states[i+1] == active:
                    temp.append(active)
            elif i == len(states) - 1:
                if states[i-1] == inactive:
                    temp.append(inactive)
                if states[i-1] == active:
                    temp.append(active)
            else:
                if states[i-1] == states[i+1]:
                    temp.append(inactive)
                else:
                    temp.append(active)
        states = temp
        
    
    return states

print(cellCompete([1, 1, 1, 0, 1, 1, 1, 1], 2))
print(cellCompete([1, 0, 0, 0, 0, 1, 0, 0], 1))


#---- 0 1 0 0 1 0 1 0 ----#