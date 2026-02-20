import pandas as pd
from scrape_live_odds import scrape_live_odds
from margin_removal import remove_margin
from weighted_consensus import weighted_consensus
from bookmaker_weights import BOOKMAKER_WEIGHTS
from calculate_edge import calculate_edge


def build_dataset(data):

    rows = []

    for event in data:

        event_name = f"{event['home_team']} vs {event['away_team']}"

        for book in event["bookmakers"]:

            book_name = book["key"]

            for market in book["markets"]:

                outcomes = market["outcomes"]

                odds = [o["price"] for o in outcomes]

                if len(odds) != 2:
                    continue

                fair_odds = remove_margin(odds)

                for outcome, raw_odds, fair_o in zip(outcomes, odds, fair_odds):

                    rows.append({
                        "event": event_name,
                        "team": outcome["name"],
                        "book": book_name,
                        "decimal_odds": raw_odds,
                        "true odds": fair_o,
                        "book_prob": 1 / raw_odds,
                        "true_prob": 1 / fair_o
                    })

    return pd.DataFrame(rows)


if __name__ == "__main__":

    data = scrape_live_odds()

    df = build_dataset(data)

    df = weighted_consensus(df, weights=BOOKMAKER_WEIGHTS)

    df = calculate_edge(df)

    df = df.sort_values("ev", ascending=False)

    print("\nTop 10 Opportunities by Expected Value:\n")
    print(
        df[[
            "event",
            "team",
            "book",
            "decimal_odds",
            "ev",
            "z_score"
        ]].head(10)
    )