# pattern_consolidation.py
# This is gateway to the pattern file.
"""
Herein, the Blueprint implementation of the pattern will go, which in turn would be consolidated by the
individual patterns.
This structure makes it easier to find the code and resources needed for a given functionality.
Input:
The call can come to this file specifying:
    one or more tickers
    one or more patterns
    period
    frequency

Output:
Multiple Dataframes one corresponding to each pattern; since pattern can have their specific dimensions.
"""
