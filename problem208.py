from itertools import product

all_peters_scores = sorted([sum(i) for i in product(*[[1, 2, 3, 4]] * 9)])
all_colins_scores = sorted([sum(i) for i in product(*[[1, 2, 3, 4, 5, 6]] * 6)])

peters_possible_scores = list(frozenset(all_peters_scores))
peters_hashed_scores = dict((
    (val, all_peters_scores.count(val))
    for val in peters_possible_scores))

colins_possible_scores = list(frozenset(all_colins_scores))
colins_hashed_scores = dict((
    (val, all_colins_scores.count(val))
    for val in colins_possible_scores))

wins = 0
for peter_score_value, peter_score_count in reversed(peters_hashed_scores.items()):
    for colin_score_value, colin_score_count  in colins_hashed_scores.items():
        if peter_score_value > colin_score_value:
            wins += colin_score_count * peter_score_count
        else:
            break


total = len(all_peters_scores) * len(all_colins_scores)
print "Wins:", wins
print "Totals:", total
print round(wins * 1.0 / total, 7)
