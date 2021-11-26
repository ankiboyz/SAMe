# JSM!!!
# SAMe - Stocks Algorithms Model ensemble.

The Project is built with following ideologies:
1. Every Pattern:
    - can have it's own dimensions which are specific to that pattern itself.
    - can also have different input parameters. (for example Moving Average Pattern can have type as SMA, EMA, EWMA etc.)

2. Pattern will emit out a signal - Signal can have a canonical structure, so that it can serve as an agnostic interface.


Some limitations v1.0:
1. The scope of data is taken to be within last 60 days as that is where the yf library can provide
the datetime data to the minute. 
Eventually 
    - need to persist the datetime data in the data storage - can be used for back testing / model learning.
    - the real time data for the minute for intra day can be gathered through other real time APIs.
    - interval minute wise is supported only if the start and end dates are within 60 days.
    - if the analysis is within 60 days then we can do the intra-day or minute wise analysis.



Ideologies:
    - Need to aim at 100% test coverage.
    - Every service i.e. every url need to have tests corresponding to those, 
      even the internal methods would be having the test coverage.