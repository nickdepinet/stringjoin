stringjoin
==========

This is meant as a basic speed comparison between python's + and String.join() methods. It is based on Wayne Werner's Stack Overflow answer here: http://stackoverflow.com/a/3055558. I've attempted to correct for some inefficiencies caused by him doing a .append when testing join.

To run:
original:
    python stringconcat.py
my fix:
    python stringfixed.py
    
Not meant to be anything super qualitative, just a useful little test of strings of different lengths.
