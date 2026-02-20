def weighted_consensus(df, weights=None):

    if weights is None:
        df["weight"] = 1.0
    else:
        df["weight"] = df["book"].map(weights).fillna(1.0)

    df["weighted_prob"] = df["true_prob"] * df["weight"]

    grouped = (df.groupby(["event", "team"]).agg(total_weighted_prob=("weighted_prob", "sum"),total_weight=("weight", "sum")))

    grouped["consensus_prob"] = (grouped["total_weighted_prob"] / grouped["total_weight"])

    grouped = grouped.reset_index()[["event", "team", "consensus_prob"]]

    return df.merge(grouped, on=["event", "team"])