Sportsbook Consensus Model



This model looks for edges in NBA moneyline markets using live odds from The Odds API.







The model:



* Pulls live decimal odds



* Removes bookmaker margins



* Calculates a weighted consensus true probability



* Calculates expected value (EV) and other metrics



* Returns selections with the largest EV (even if negative)







Methodology



* Margin Removal

&nbsp;	Implied probability = 1 / book odds

&nbsp;	Margin = sum of implied probabilities - 1



&nbsp;	Margin is removed using this formula for proportional adjustment:



&nbsp;	True odds = (n \* book odds) / (n - book odds \* margin)

&nbsp;	n = number of selections (2 selections in our market)



&nbsp;	True probability = 1 / true odds





* Weighted Consensus

&nbsp;	Consensus probability = weighted average of true probabilities of a selection across books

&nbsp;	Default weights = 1 for all books. Can be changed from bookmakers\_weights.py





* Edge Calculation

&nbsp;	Expected Value (EV): EV = (Consensus probability \* odds) − 1

&nbsp;	Positive EV indicates a potential value bet.

&nbsp;	Log growth for long term wealth growth

&nbsp;	Z score for statistical significance







How To Run



* Install requirements: pip install -r requirements.txt



* Add API Key in the config.py



* Run main.py



