num_candidates = int(input())

candidates = {}
for c in range(num_candidates):
    candidate = input()
    party = input()
    if party == '':
        candidates[candidate] = 'independent'
    else:
        candidates[candidate] = party

num_votes = int(input())

votes = []
for v in range(num_votes):
    vote = input()
    if vote in candidates:
        votes.append(vote)
    else:
        pass

votes_candidate = {}
for c in votes:
    if c not in votes_candidate:
        votes_candidate[c] = 1
    else:
        votes_candidate[c] += 1


votes_candidate = sorted(votes_candidate.items(), key=lambda x: x[1], reverse=True)

if votes_candidate[0][1] != votes_candidate[1][1]:
    winner = candidates[votes_candidate[0][0]]
else:
    winner = 'tie'
print(winner)