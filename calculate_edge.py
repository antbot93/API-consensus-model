import numpy as np


def calculate_edge(df):

    # Raw probability edge
    df["prob_edge"] = df["consensus_prob"] - df["book_prob"]

    # Expected value
    df["ev"] = (df["consensus_prob"] * df["decimal_odds"]) - 1

    # Log return edge
    df["log_edge"] = np.log(df["decimal_odds"] * df["consensus_prob"])

    # Cross-book dispersion
    std_dev = (df.groupby(["event", "team"])["true_prob"].std().reset_index().rename(columns={"true_prob": "std_dev"}))

    df = df.merge(std_dev, on=["event", "team"])

    # Z-score deviation
    df["z_score"] = ((df["true_prob"] - df["consensus_prob"]) / df["std_dev"])

    return df