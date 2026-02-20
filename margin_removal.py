def remove_margin(book_odds):

    # Removes bookmaker margin using proportional adjustment.
    # Assumes 2-outcome market.

    implied_probs = [1 / o for o in book_odds]
    margin = sum(implied_probs) - 1

    true_odds = [(2 * o) / (2 - (margin * o)) for o in book_odds]

    return true_odds