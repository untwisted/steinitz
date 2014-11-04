steinitz
========

A chess interface to fics with support for stockfish to analyze moves.

I always was enthusiasmed with chess, i played years on fics.
Fics is a nice server although it is a well known fact that there exists the worse
kind of cheaters. They use engine to get off bad positions all time.

As going through the game entirely then checking my opponent players move is massive,
i thought of implementing steinitz that is a complete chess interface to fics.
Steinitz permits you to check the next move of your opponent with stockfish actually.

Steinitz stockfish plugin permits you to score your opponent move and your move 
when it is played. Such a tool permits you to improve your tactical skills.

With steinitz, ironically it is possible to tell stockfish to play for you. 
It is useful when examining games on fics. You could examine of your games
then ask stockfish for which was the best move at a given position.

It is true that it gives you opportunity to cheat but it will not make you a great player 
nor enjoy the truely sense of chess that is: on the board you can't lie to yourself.

Install
=======

This is a short script to run the latest version of steinitz.

    cd /tmp
    
    git clone git://git.code.sf.net/p/untwisted/code untwisted-code
    cd untwisted-code
    python setupp.py install
    
    cd steinitz-code
    git clone git@github.com:iogf/steinitz.git steinitz-code
    python setup.py install

Videos
======
https://www.youtube.com/watch?v=xv71Cmg_8pc&feature=youtu.be

Observation
===========
Steinitz is under development, it was on sourceforge then i decided to bring it to github
for some reasons. 

There remains some features to be implemented, some of the menus don't work.
Steinitz is 95% done.


Old Repository
==============
git clone ssh://olliveira@git.code.sf.net/p/steinitz/code steinitz-code

