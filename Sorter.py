#!/usr/bin/env python
# coding: utf-8

# In[1]:


import statistics


# In[2]:


f = open("poker-hands.txt", "r")
file = f.read()
input_arr = []
for each in file.split("\n"):
    input_arr.append(each)


# In[3]:


def card(list1):
    l1 = []
    for each in list1:
        if(each[0] == 'T'):
            temp = '10'
        elif(each[0] == 'J'):
            temp = '11'
        elif(each[0] == 'Q'):
            temp = '12'
        elif(each[0] == 'K'):
            temp = '13'
        elif(each[0] == 'A'):
            temp = '14'
        else:
            temp = each[0]
        l1.append(int(temp))
    return(l1)


# In[4]:


def suit(list1):
    l1 = []
    for each in list1:
        l1.append(each[1])
    return(l1)


# In[5]:


def max_freq(l1):
    res = statistics.mode(l1)
    return(l1.count(res))


# In[6]:


def rank_rule(p_card, p_suit):
    p_card.sort()
    
    # Royal Flush
    if( (len(set(p_suit)) == 1) and ( p_card == [10, 11, 12, 13, 14] ) ):
        return(10)
    # Straight flush
    elif( (len(set(p_suit)) == 1) and ( (max(p_card) - min(p_card)) == 4 ) and (len(set(p_card)) == 5) ):
        return(9)
    # 4 of a kind
    elif( (len(set(p_card)) == 2) and ( (p_card[1] == p_card[2]) and (p_card[2] == p_card[3]) ) ):
        return(8)
    # Full house
    elif( len(set(p_card)) == 2 ):
        return(7)
    # Flush
    elif( (len(set(p_suit)) == 1) ):
        return(6)
    # Straight
    elif( ( (max(p_card) - min(p_card)) == 4 ) and (len(set(p_card)) == 5) ):
        return(5)
    # 3 of a kind
    elif( max_freq(p_card) == 3 ):
        return(4)
    # 2 pairs
    elif( len(set(p_card)) == 3 ):
        return(3)
    # 1 pair
    elif( len(set(p_card)) == 4 ):
        return(2)
    # high card
    else:
        return(1)
        


# In[7]:


def high_Card(p1_card, p2_card):
    p1_card.sort()
    p2_card.sort()
    
    for i in range(0, len(p1_card)):
        if(p1_card[i] > p2_card[i]):
            return(1)
        elif(p1_card[i] < p2_card[i]):
            return(2)
    return(0)


# In[8]:


def tie_result(p1_card, p1_suit, p2_card, p2_suit, rank):
    # Royal Flush
    if(rank == 10):
        return("Tie")
    # Straight flush
    elif(rank == 9):
        t_win = high_Card(p1_card, p2_card)
        if(t_win == 1):
            return("p1 wins")
        elif(t_win == 2):
            return("p2 wins")
        else:
            return("Tie")
    # 4 of a kind
    elif(rank == 8):
        p1 = [f for f in set(p1_card) if p1_card.count(f) == 4][0]
        p2 = [f for f in set(p2_card) if p2_card.count(f) == 4][0]

        if(p1>p2):
            return("p1 wins")
        elif(p1<p2):
            return("p2 wins")
        else:
            return("Tie")

    # Full house
    elif(rank == 7):
        p1 = [f for f in set(p1_card) if p1_card.count(f) == 3][0]
        p2 = [f for f in set(p2_card) if p2_card.count(f) == 3][0]

        if(p1>p2):
            return("p1 wins")
        elif(p1<p2):
            return("p2 wins")
        else:
            t_win = high_Card(p1_card, p2_card)

            if(t_win == 1):
                return("p1 wins")
            elif(t_win == 2):
                return("p2 wins")
            else:
                return("Tie")

    # Flush
    elif(rank == 6):
        t_win = high_Card(p1_card, p2_card)
        if(t_win == 1):
            return("p1 wins")
        elif(t_win == 2):
            return("p2 wins")
        else:
            return("Tie")
    # Straight
    elif(rank == 5):
        t_win = high_Card(p1_card, p2_card)
        if(t_win == 1):
            return("p1 wins")
        elif(t_win == 2):
            return("p2 wins")
        else:
            return("Tie")
    # 3 of a kind
    elif(rank == 4):
        p1 = [f for f in set(p1_card) if p1_card.count(f) == 3][0]
        p2 = [f for f in set(p2_card) if p2_card.count(f) == 3][0]

        if(p1>p2):
            return("aa")
        elif(p1<p2):
            return("p2 wins")
        else:
            t_win = high_Card(p1_card, p2_card)

            if(t_win == 1):
                return("p1 wins")
            elif(t_win == 2):
                return("p2 wins")
            else:
                return("Tie")


    # 2 pairs
    elif(rank == 3):
        p1 = [f for f in set(p1_card) if p1_card.count(f) == 2]
        p2 = [f for f in set(p2_card) if p2_card.count(f) == 2]

        t_win = high_Card(p1_card, p2_card)
        if(t_win == 1):
            return("p1 wins")
        elif(t_win == 2):
            return("p2 wins")
        else:
            p1 = [f for f in set(p1_card) if p1_card.count(f) == 1][0]
            p2 = [f for f in set(p2_card) if p2_card.count(f) == 1][0]

            if(p1>p2):
                return("p1 wins")
            elif(p1<p2):
                return("p2 wins")
            else:
                return("Tie")

    # 1 pair
    elif(rank == 2):

        p1 = [f for f in set(p1_card) if p1_card.count(f) == 2]
        p2 = [f for f in set(p2_card) if p2_card.count(f) == 2]
        
        if(p1>p2):
            return("p1 wins")
        elif(p1<p2):
            return("p2 wins")
        else:
            t_win = high_Card(p1_card, p2_card)

            if(t_win == 1):
                return("p1 wins")
            elif(t_win == 2):
                return("p2 wins")
            else:
                return("Tie")

    # high card
    else:
        t_win = high_Card(p1_card, p2_card)
        if(t_win == 1):
            return("p1 wins")
        elif(t_win == 2):
            return("p2 wins")
        else:
            return("Tie")


# In[9]:


# rule for win:

def win_logic(p1_hand, p2_hand):
    
    p1_card = card(p1_hand)
    p1_suit = suit(p1_hand)
    p2_card = card(p2_hand)
    p2_suit = suit(p2_hand)
        
    if(rank_rule(p1_card, p1_suit) > rank_rule(p2_card, p2_suit)):
        out = ("p1 wins")
    elif(rank_rule(p1_card, p1_suit) == rank_rule(p2_card, p2_suit)):
        out = tie_result(p1_card, p1_suit, p2_card, p2_suit, rank_rule(p2_card, p2_suit))
    else:
        out = ("p2 wins")

    return(out)


# In[10]:


p1 = 0
p2 = 0

for each in input_arr:
    
    p1_hand = each.split(" ")[0:5]
    p2_hand = each.split(" ")[5:10]
    result = win_logic(p1_hand, p2_hand)
    
    if(result == "p1 wins"):
        p1 = p1 + 1
    else:
        p2 = p2 + 1


# In[11]:


print("p1 wins:", p1, "\np2 wins:", p2)

