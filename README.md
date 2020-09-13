# alliums-Melakarta-Ragas-in-Interval-Ratios
The 72 Melakarta Ragas of Carnatic music expressed in the form of interval ratios. 

A raga can be thought of like a scale. Given a tonic note, a raga determines the distances between the tonic and the rest of the swaras in the raga.

The intention of this project is twofold.
1. To advance and proliferate the study of Carnatic music by converting an essential building block of the art form to a format that can be easily utilized in synthesis.
2. To create a lightweight script that anyone can use to convert music from Carnatic swaras to the universal, mathematically impartial system of interval notation.

This was designed with sound synthesis in mind, specifically to quantize scales on modular synthesizers like the Expert Sleepers Disting Mk4 and Minilogue. Some Carnatic scales were already available, like on the Mutable Instruments Marbles, but I thought there should be a full bank of scales. Even the 4,000 Scala scales have only 2 of the Melakarta Ragas. My goal is to have all of the essential ragas in with all of their harmonic variations different versions in .scl format in the public domain.

On the translation script:

Input should come from a .txt file. Put each scale on a separate line. Separate each note by a space.
Each note should have one letter and one number - except for S, P, and Ṡ. 
For now, capital letters only. Because Carnatic music is commonly written using subscript for the numbers, subscript numbers are accepted.

Acceptable input notes look like: 
S R₁ G1 M₁ P D2 N₃ Ṡ
Unacceptable:
R 1 n2 m1 N4 

A line of output looks something like:
1 32/31 32/27 4/3 3/2 128/81 16/9 2 


For now, this project uses 16 distinct swaras that are identified by specific intervals from the root note by way of interval ratios. You can find these ratios in the ratioDict.py file.

Yeah, it's a mess, i'm working on it. 

Eventually I am planning on implementing:
1. Directly output scales to individual, formatted .scl files
2. Alternate tunings

