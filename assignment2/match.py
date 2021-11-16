import numpy as np
from numpy import random
from typing import List, Tuple

def run_matching(scores: List[List], gender_id: List, gender_pref: List) -> List[Tuple]:




    #does friendship matching and disregards gender preferences


    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    random.shuffle(arr)
    recievers = arr[0:5]
    proposers = arr[5:10]
    print(recievers)
    print(proposers)
    #we keep track of pairs by putting proposers in and out of the array "pairs" which is indexed by the recievers, eg. the proposer 
    #in spot 0 is paired with the reciever in spot 0 of the recievers array
    print(scores[0])
    preferences = np.zeros( (5, 5))
    for i in range(0,5):
        for j in range(0,5):
            preferences[i][j] = j
        #use a variation of bubble sort to figure out each proposer's preference order
        #here preferences[i][j] is the index of the reciever (in the recievers array) that is proposer[i]'s jth choice
        for k in range(0, 7):
            for j in range(0, 4):
                if scores[proposers[i]-1][recievers[int(preferences[i][j])]-1] < scores[proposers[i]-1][recievers[int(preferences[i][j+1])]-1]:
                    nothing = preferences[i][j]
                    preferences[i][j] = preferences[i][j+1]
                    preferences[i][j+1] = nothing
    pairs = np.zeros(5)
    matched = np.zeros(5)
    finished = False
    while finished == False:
        finished = True
        #i is the index of the proposer, matched keeps track of which proposers have been matched
        for i in range(0,5):
            if matched[i] == 0:
                finished = False
                for nthPreference in range(0,5):
                    recieverIndex = int(preferences[i][int(nthPreference)])
                    if pairs[recieverIndex] == 0:
                        if matched[i] == 0:
                            pairs[recieverIndex] = i
                            matched[i] = 1
                            print("hooi")
                    if scores[recievers[recieverIndex]-1][proposers[int(pairs[recieverIndex])] - 1] < scores[recievers[recieverIndex]-1][proposers[i] - 1]:
                        if matched[i] == 0:
                            print("huh")
                            matched[int(pairs[recieverIndex])] = 0
                            pairs[int(recieverIndex)] = i
                            matched[i] = 1
    print("preferences: ")
    print(preferences)
    print("matches: " + str(pairs))   
    print("pair 1: " + str(recievers[0]) + " " + str(proposers[int(pairs[0])]))
    print("pair 2: " + str(recievers[1]) + " " + str(proposers[int(pairs[1])]))
    print("pair 3: " + str(recievers[2]) + " " + str(proposers[int(pairs[2])]))
    print("pair 4: " + str(recievers[3]) + " " + str(proposers[int(pairs[3])]))
    print("pair 5: " + str(recievers[4]) + " " + str(proposers[int(pairs[4])]))



    """
    TODO: Implement Gale-Shapley stable matching!
    :param scores: raw N x N matrix of compatibility scores. Use this to derive a preference rankings.
    :param gender_id: list of N gender identities (Male, Female, Non-binary) corresponding to each user
    :param gender_pref: list of N gender preferences (Men, Women, Bisexual) corresponding to each user
    :return: `matches`, a List of (Proposer, Acceptor) Tuples representing monogamous matches

    Some Guiding Questions/Hints:
        - This is not the standard Men proposing & Women receiving scheme Gale-Shapley is introduced as
        - Instead, to account for various gender identity/preference combinations, it would be better to choose a random half of users to act as "Men" (proposers) and the other half as "Women" (receivers)
            - From there, you can construct your two preferences lists (as seen in the canonical Gale-Shapley algorithm; one for each half of users
        - Before doing so, it is worth addressing incompatible gender identity/preference combinations (e.g. gay men should not be matched with straight men).
            - One easy way of doing this is setting the scores of such combinations to be 0
            - Think carefully of all the various (Proposer-Preference:Receiver-Gender) combinations and whether they make sense as a match
        - How will you keep track of the Proposers who get "freed" up from matches?
        - We know that Receivers never become unmatched in the algorithm.
            - What data structure can you use to take advantage of this fact when forming your matches?
        - This is by no means an exhaustive list, feel free to reach out to us for more help!
    """
    matches = [(recievers[0], proposers[int(pairs[0])]), (recievers[1], proposers[int(pairs[1])]), (recievers[2], proposers[int(pairs[2])]), (recievers[3], proposers[int(pairs[3])]), (recievers[4], proposers[int(pairs[4])])]
    return matches

if __name__ == "__main__":
    raw_scores = np.loadtxt('raw_scores.txt').tolist()
    genders = []
    with open('genders.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            genders.append(curr)

    gender_preferences = []
    with open('gender_preferences.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            gender_preferences.append(curr)

    gs_matches = run_matching(raw_scores, genders, gender_preferences)
