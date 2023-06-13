import random

class SocialCircle():
    '''
    Class for a new social circle which includes all the user's current friends.
    
    __init__
    Parameters
    ------
    name : string, default = Bingus
    
    friends : dictionary, optional
    Initial list of friends
    
    Instance Attributes
    ------
    self.name : string, default = bingus
    Name of the person who the social circle belongs to
    
    self.friends : dictionary, optional, default: empty dict {}
    List of friends in the social circle. Each friend has a rating 1-5
    
    self.friend_score : int
    Sum of all friend ratings in self.friends
    
    '''
    def __init__(self, name = 'Bingus', friends = {}):
        self.name = name
        self.friends = friends
        self.friend_score = self.get_friend_score()
        print('Welcome to your social circle, ' + self.name + '!\n')
        
    def __str__(self):
        # So name shows up as default string when object is called
        return self.name
        
    def friends_list(self):
        '''
        Prints the current list of friends and their ratings.
        
        Parameters: None
        
        Returns: None
        
        '''
        friends_list = '\n' + self.name + '\'s current list of friends:\n'
        
        # If there are no items in self.friends
        if len(self.friends) < 1:
            friends_list = 'Looking pretty lonely...\n'
            
        # If there is 1 or more item in self.friends
        else:
            for ind in self.friends:
                # Prints friend in format of "Friend (rating)" for all friends in self.friends
                friends_list += ind + ' (' + str(self.friends[ind]) + ')\n'
            
        # Total friend score of current friends list
        friends_list += 'Friend Score: ' + str(self.friend_score) + '\n'
        return friends_list
        
    def get_friend_score(self):
        '''
        Adds up all friend ratings for a cumulative friend score.
        
        Parameters: Self
        
        Returns
        -----
        self.friend_score : int
        Sum of all friend ratings in self.friends
        
        '''
        # Totals the ratings of all friends
        self.friend_score = 0
        temp = 0
        for friend in self.friends:
            temp += self.friends[friend]
            
        # Updates and returns self.friend_score
        self.friend_score = temp
        return self.friend_score
        
    def add_friend(self, friend, rating = 3):
        '''
        Adds a friend to the social circle. Prints a message along with it.
        
        Parameters
        ------
        friend : string
        Name of the new friend
        
        rating : int, default = 3
        Friend's associated rating
        
        Returns
        -------
        new_pos: list
        Coordinates of the next position for Bingus as [row, column]
        
        '''
        # Adds friend to self.friends
        self.friends[friend] = rating
        
        # Custom message based on initial friend rating
        if rating < 3:
            print(friend + ' is now your friend. Looks like they didn\'t make a good first impression...')
        elif rating > 3:
            print(friend + ' is now your friend! They seem to have made a great first impression :)')
        else:
            print(friend + ' is now your friend!')
            
        # Updates friend score
        self.get_friend_score()
            
    def ghost_friend(self):
        '''
        Ghosts friends who fall below a friend rating of 1.
        
        Parameters: None
        
        Returns
        -------
        Edits the friends instance field by deleting friends with ratings lower than 1
        
        '''
        # Creates list of friends to delete
        delete = []
        for friend, rating in self.friends.items():
            if rating == 0:
                delete.append(friend)

        # Deletes friends from self.friends
        if len(delete) > 0:
            for friend in delete:
                self.friends.pop(friend)
                print(friend + ' is no longer your friend.\n')

        # Updates friend score
        self.get_friend_score
            
    def hangout(self, group, fun = True):
        '''
        Updates friend ratings after a hangout.
        
        Parameters
        -------
        group : list
        List of friends (strings) involved in the hangout
        
        fun : boolean, default = True
        Whether the hangout was fun or not. Increases/decreases friend ratings respectively
        
        Returns: None
        '''
        # Custom message based on group and fun level
        hangout_str = 'You hang out with:\n'
        for friend in group:
            hangout_str += friend + '\n'
        if fun:
            hangout_str += 'It was fun!'
        else:
            hangout_str += 'It wasn\'t very fun...'
        print(hangout_str)
        
        # Adds 1 to friend rating if hangout was fun, subtracts 1 if hangout was not
        if fun:
            for ind in group:
                if ind not in self.friends:
                    self.add_friend(ind)
                elif self.friends[ind] < 5:
                    self.friends[ind] += 1
        else:
            for ind in group:
                if ind not in self.friends:
                    print('Remind yourself not to hang out with ' + ind + ' again...\n')
                else:
                    self.friends[ind] -= 1
        
        # Deletes friends whose ratings fell below 1 after the hangout, updates friend score
        self.ghost_friend()
        self.get_friend_score()
        
    def bored(self):
        '''
        You're bored and want to see a friend. You randomly hit up one of your friends for a hangout!
        
        Parameters: None
        
        Returns
        ------
        Depending on hangout result, can shorten the list of friends
        
        '''
        # Custom message if self.friends is empty
        if len(self.friends) < 1:
            print('\nYou have no one to hang out with...\n')
        
        # Creates a random index in the dictionary to choose from
        else:
            start = 0
            end = random.randint(0, len(self.friends)-1)
            
            # Selects a random friend with the chosen index
            for friend in self.friends:
                if start != end:
                    start += 1
                    continue
                else:
                    hangout_buddy = friend
                    break
            # Print statement specifying the hangout buddy
            print('\nYou\'re bored and decide to hang out with ' + hangout_buddy + ' for today.')

            # Calculates fun, fun increases if hangout buddy's friend rating is higher
            fun_chance = random.randint(1, 5) * self.friends[hangout_buddy]
            
            # Multiplication comes up with 17 results, 6 being the median
            if fun_chance > 6:
                result = True
            else:
                result = False
                
            # Calls the hangout method to adjust friend ratings based on the hangout
            self.hangout([hangout_buddy], fun = result)
            
        