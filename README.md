API Consensus Model



This model looks for edges in NBA moneyline markets using live odds from The Odds API.







The model:



* Pulls live decimal odds



* Removes bookmaker margins



* Calculates a weighted consensus true probability



* Calculates expected value (EV) and other metrics



* Returns selections with the largest EV (even if negative)







Methodology



* Margin Removal

 	Implied probability = 1 / book odds

 	Margin = sum of implied probabilities - 1



 	Margin is removed using this formula for proportional adjustment:



 	True odds = (n \* book odds) / (n - book odds \* margin)

 	n = number of selections (2 selections in our market)



 	True probability = 1 / true odds





* Weighted Consensus

 	Consensus probability = weighted average of true probabilities of a selection across books

 	Default weights = 1 for all books. Can be changed from bookmakers\_weights.py





* Edge Calculation

 	Expected Value (EV): EV = (Consensus probability \* odds) − 1

 	Positive EV indicates a potential value bet.

 	Log growth for long term wealth growth

 	Z score for statistical significance







How To Run



* Install requirements: pip install -r requirements.txt



* Add API Key in the config.py



* Run main.py
