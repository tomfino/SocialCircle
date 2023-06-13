def compare_popularity(person1, person2):
    '''
    Compares popularity based on friend scores between person1 and person2. Initially this function returned
    the more popular person for more complex uses, but I had it return a string instead as it's all we need for now.
    
    Parameters
    ------
    person1 : SocialCircle object
    
    person2 : SocialCircle object
    
    Returns
    ------
    winner : string
    Returns a statement claiming the more popular person
    
    '''
    # Retrieves the friend scores of each person
    pop1 = person1.get_friend_score()
    pop2 = person2.get_friend_score()
    difference = abs(pop1-pop2)
    
    if pop1 > pop2:
        winner = str(person1) + ' is more popular than ' + str(person2) + ' by ' + str(difference) + ' friend points!'
        return winner
    elif pop2 > pop1:
        winner = str(person2) + ' is more popular than ' + str(person1) + ' by ' + str(difference) + ' friend points!'
        return winner
    else:
        winner = str(person1) + ' and ' + str(person2) + ' are equally as popular! Such a shame.'
        return winner