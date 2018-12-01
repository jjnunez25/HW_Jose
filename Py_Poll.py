# import os and write csv path
import os
import csv

path = os.path.join("election_data_2.csv")

with open(path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    # lists to append
    voterid = []
    county = []
    candidates = []

    for dog in csvreader:
        voterid.append(dog[0])
        county.append(dog[1])
        candidates.append(dog[2])

    canset = set(candidates)
    totalvote = len(voterid)
    cnt = Counter(candidates)

    # create a list with the unique names
    can_names = []

    for row in canset:
        can_names.append(row)

    print("Election Results")
    print("----------------------------------------")
    print(f"The total number of votes was {tot_vote}")
    print("----------------------------------------")

    dictionarycan = {}
    cancount = 0
    for row in can_names:
        candidate_name = str(can_names[can_count])
        votes = candidates.count(candidate_name)
        votes = int(votes)
        percentage = round(votes / tot_vote * 100, 2)
        dictionary_can.update({candidate_name: votes})
        print(f"{candidate_name}: {percentage}%  ({votes} votes)")
        can_count = can_count + 1

    winner = max(dictionary_can, key=lambda key: dictionary_can[key])

    print("Winner: ", winner)







