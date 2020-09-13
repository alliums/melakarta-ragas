# alliums-Melakarta-Ragas-in-Interval-Ratios
The 72 Melakarta Ragas of Carnatic music expressed in the form of interval ratios. 

A raga is basically a melodic mode. Among other things, it provides musical key, a framework for harmony by way of determining proportions of space between notes.

The intention of this project is twofold.
1. To advance and proliferate the study of Carnatic music by converting some of the essential building blocks of the harmonic framework of the system to a format that can be easily utilized in synthesis and sequencing.
2. To create a lightweight script that anyone can use to convert written music from Carnatic swaras to the universal, mathematically impartial system of interval notation.

This was designed with sound synthesis in mind, specifically to quantize scales, chords, and arpeggios. Some Carnatic scales were already available, like on the Mutable Instruments Marbles, but there are far from enough. The popular Scala database of 4,00 samples contains only 2 of the Melakarta Ragas. My goal is to have a comprehensive offering of the essential ragas in with all of their harmonic variations different versions in .scl format in the public domain for anyone to use.


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
