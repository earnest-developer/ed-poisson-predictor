import numpy


def predict_on_ave_pair_scores(
    ave_home_scored: float, ave_away_scored: float, simulations: int = 1000
):
    """ Predicts match outcome odds based on goals scored by the teams against each other """

    possible_outcomes = numpy.full(simulations, "X", dtype=str)

    for iteration in range(simulations):

        h_scored_predicted = numpy.random.poisson(lam=ave_home_scored, size=None)
        a_scored_predicted = numpy.random.poisson(lam=ave_away_scored, size=None)

        possible_outcomes[iteration] = map_outcome_from_score(
            h_scored_predicted, a_scored_predicted
        )

    return map_odds_from_possible_outcomes(possible_outcomes)


def predict_on_ave_team_scores(
    ave_scored_home: float,
    ave_conceded_home: float,
    ave_scored_away: float,
    ave_conceded_away: float,
    simulations: int = 1000,
):
    """ Predicts match outcome odds based on goals scored/conceited by each team """

    possible_outcomes = numpy.full(simulations, "X", dtype=str)

    for iteration in range(simulations):

        h_scored_predicted = numpy.random.poisson(
            lam=1 / 2 * (ave_scored_home + ave_conceded_away), size=None
        )

        a_scored_predicted = numpy.random.poisson(
            lam=1 / 2 * (ave_scored_away + ave_conceded_home), size=None
        )

        possible_outcomes[iteration] = map_outcome_from_score(
            h_scored_predicted, a_scored_predicted
        )

    return map_odds_from_possible_outcomes(possible_outcomes)


def map_outcome_from_score(home_score: int, away_score: int):
    """Returns a letter indicating the outcome (Draw, Home, Away)"""

    if home_score == away_score:
        return "D"
    if home_score > away_score:
        return "H"
    else:
        return "A"


def map_odds_from_possible_outcomes(possible_outcomes: numpy.ndarray):
    """Calculates the odds for each outcome based on the number of possible outcomes"""

    outcomes, counts = numpy.unique(possible_outcomes, return_counts=True)

    odds = numpy.around(counts / len(possible_outcomes), decimals=3)

    return dict(zip(outcomes, odds))


# Mock predictor of Arsenal vs Southampton
# EPL	2/23/2019	 15:00	Arsenal V Southampton	Arsenal	Southampton	0.5584	0.2362	0.2054
# EPL	2/23/2019	 15:00	Arsenal V Southampton	Arsenal	Southampton	0.5585	0.2348	0.2067
# EPL	2/23/2019	 15:00	Arsenal V Southampton	Arsenal	Southampton	0.5565	0.2398	0.2037
# EPL	2/23/2019	 15:00	Arsenal V Southampton	Arsenal	Southampton	0.8631	0.1097	0.0272
# EPL	2/23/2019	 15:00	Arsenal V Southampton	Arsenal	Southampton	0.8739	0.0972	0.0289
average_home_scored_against_pair = 2.3333333
average_away_score_against_pair = 0.6666667
number_of_matches_against_each_other = 3

average_scored_h = 2.1052632
average_conceded_h = 0.8355263
average_scored_a = 1.0789474
average_conceded_a = 1.359649

dummy = predict_on_ave_pair_scores(
    average_home_scored_against_pair, average_away_score_against_pair
)

# dummy1 = predict_on_ave_team_scores(
#     average_scored_h, average_conceded_h, average_scored_a, average_conceded_a
# )

print(dummy)
# print(dummy1)

# results, counts = numpy.unique(possible_outcomes, return_counts=True)
