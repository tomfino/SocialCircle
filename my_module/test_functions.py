'''
Test for my functions.

Many of my functions include print statements which have been tested as well.
'''

from my_module.classes import SocialCircle
from my_module.functions import *

# Because I'm too lazy to copy paste the test calls
def test_the_tests():
    test_str()
    test_get_friend_score()
    test_compare_popularity()
    test_hangout()
    test_bored()

def test_str():

    test1 = SocialCircle('Mark')
    assert str(test1) == 'Mark'
    
    test2 = SocialCircle()
    assert str(test2) == 'Bingus'

def test_get_friend_score():

    test1 = SocialCircle()
    test1.add_friend('Angelo', 5)
    test1.add_friend('Shawn', 1)
    assert test1.get_friend_score() == 6
    test1.add_friend('Alex', 2)
    test1.add_friend('CJ', 3)
    assert test1.get_friend_score() == 11
    test1.hangout(['CJ'], fun = False)
    assert test1.get_friend_score() == 10
    
    test2 = SocialCircle()
    test2.add_friend('Matthew', 1)
    test2.add_friend('Cory', 1)
    assert test2.get_friend_score() == 2
    test2.add_friend('Jarrett', 1)
    test2.add_friend('Caleb', 3)
    assert test2.get_friend_score() == 6
    
def test_compare_popularity():
    
    test1 = SocialCircle()
    test1.add_friend('Finn', 5)
    test1.add_friend('Jake', 1)
    
    test2 = SocialCircle()
    test2.add_friend('Princess Bubblegum', 1)
    test2.add_friend('Marceline', 1)
    
    test3 = SocialCircle()
    test3.add_friend('Ice King', 1)
    test3.add_friend('Gunter', 1)
    
    assert compare_popularity(test1, test2) == test1
    assert compare_popularity(test3, test2) == None
    
def test_hangout():
    test1 = SocialCircle()
    test1.add_friend('Mike', 5)
    test1.add_friend('Daniel', 1)
    
    test1.hangout(['Daniel', 'Mike'], fun = False)
    assert len(test1.friends) == 1
    assert test1.friends['Mike'] == 4
    
    test1.hangout(['Mike'])
    assert test1.friends['Mike'] == 5
    
def test_bored():
    test1 = SocialCircle()
    test1.add_friend('Kai', 3)
    before_score = test1.get_friend_score()
    test1.bored()
    after_score = test1.get_friend_score()
    assert before_score != after_score
    
    
    



                 
    
