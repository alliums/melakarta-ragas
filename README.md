# melakarta-ragas

The 72 Melakarta Ragas of Carnatic music expressed in the form of interval ratios. 


Usage...

On the translation script:

Input should come from a .txt file. Put each scale on a separate line. Separate each note by a space.
Each note should have one letter and one number - except for S, P, and Ṡ, which should stand alone. 
For now, capital letters only. Because Carnatic music is commonly written using subscripts for the numbers, subscript numbers are accepted.

Acceptable input notes look like: 
S R₁ G1 M₁ P D2 N₃ Ṡ

Unacceptable:
R 1 n2 m1 N4 

A line of output looks something like:
1 32/31 32/27 4/3 3/2 128/81 16/9 2 


For now, this project uses 16 distinct swaras that are identified by specific intervals from the root note by way of interval ratios. You can find these ratios in the ratioDict.py file.

~
Yeah, it's a mess, i'm working on it. 
~

Eventually I am planning on implementing:
1. Directly output scales to individual, formatted .scl files
2. Alternate tunings

ratios from:
IJCSI International Journal of Computer Science Issues, Vol. 7, Issue 4, No 7, July 2010
ISSN (Online): 1694-0784
ISSN (Print): 1694-0814
Fundamental Frequency Estimation of Carnatic Music
Department of Computer Science and Engineering
Anna University, Chennai, India
