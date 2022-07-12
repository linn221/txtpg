### This program generates a really long password _which is a hash value_ from the combination of a phrase, a very long text file and configurations like special chars and unused chars.

How the program works?
----------------------

It can be troublesome to explain the flow in detail or maybe I can't explain very well. _(For actual detail, Plese, see the source code. It's only 50 lines long)_

### First we hash a given phrase using sha256, resulting in a series of byte, which is the immature version of the password.  
The given text file is turned into 1 and 0 based on certain critera, the computer starts reading those instructions.  
0 means we will re-hash that series of byte using sha256 and 1 means first we reverse the series of bytes (\[byte1, byte2, .., byteN\] ==> \[byteN, ... , byte2, byte1\]) , and only after that, re-hash those bytes using sha256.  

_Tips on running txtpg_
-----------------------

Use the program with cautions! If you happen to use part of the lyric of a well known song as the phrase, and a very well known book like The C Programming Language, this is not secure at all.  
  
The password has no added security if you only supply the phrase, and run the script by default. Hell, it might even be less secure because people will tend to use a weak phrase by the false sense of security.  
  
You need to use a strong phrase that is brute force proof and somewhat unguessable. Use a text file which is mysterious enough and **which will always be available to you.** You don't really need a long text, 1,000 chars is more than enough. (2 power 1000 is a really huge number) Just use a text no one else can find but you (maybe outside the internet, just **don't lose it**. _2 power 1000 is a really huge number_.)  
  
Make configurations like adding special characters and unused characters for better security. Also modify the generated password like removing a certain character or adding some. Add a capitalization rule. Map each hex digit to an another character, etc.  

* * *

_I am in no way an expert. If you find a hole in the code or the whole idea of this re-hashing the hash based on the charactes in a text book, please let me know. It is always exciting to talk about stuffs like that._