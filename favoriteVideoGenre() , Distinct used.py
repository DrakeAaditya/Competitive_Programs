def favoriteVideoGenre(numUsers, userBooksListenedTo, numGenres, bookGenres):
    # WRITE YOUR CODE HERE
    temp = {}

    def get_key(val): 
        for key, value in bookGenres.items(): 
            if val in value: 
                return key 

    def most_frequent(List): 
        if len(List) > 1:
            send = []
            for i in range(len(List)-1):
                
                if List.count(List[i]) > List.count(List[i+1]):
                    send.append(List[i])
                if List.count(List[i]) == List.count(List[i+1]):
                    send.append(List[i])
                    send.append(List[i+1])
            return send
        else:
            return List

    for i in userBooksListenedTo:
        user_list = []

        for j in userBooksListenedTo[i]:
            user_list.append(get_key(j))
        
        print(user_list)

        temp[i] = list(set(most_frequent(user_list)))
        
    return temp
    







print(favoriteVideoGenre(numUsers=3,
    userBooksListenedTo = {
        "JERRY": ["NT", "TS", "HTF"],
        "JOHN": ["L", "TW", "NT"],
        "MICHAEL": ["TW", "R"]
    },
    numGenres = 3,
    bookGenres={
        "ACTION": ["TS","R", "HTF"],
        "HISTORY": ["L", "NT"],
        "HORROR": ["TW"]
        
    }))