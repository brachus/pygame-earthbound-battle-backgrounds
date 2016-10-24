# pygame-earthbound-battle-backgrounds

This is a port of [gjtorikian's js code](https://github.com/gjtorikian/Earthbound-Battle-Backgrounds-JS) adapted
from [Mr. Accident's](https://forum.starmen.net/members/168) [Windows screensaver](https://forum.starmen.net/forum/Fan/Games/Kraken-EB-Battle-Animation-Screensaver/first) based on the battle backgrounds from Earthbound.

Ultimatley the credit goes to Nintendo, APE, and HAL Laboratory for producing Earthbound/Mother 2 in the first place.

## About the code...

For now, most of it is sloppy, with only what is needed implemented (e.g. writing routines were omitted).  Also much
of the code is kept in a single file.  I clobberd a couple classes together, like Rom with Block, mainly for
simplicity, but 

## Speed Problems 

Originally, I was having trouble getting the disortion effects/tile rendering to run efficiently.
Part of the problem was of how limited pygame is in options taking in arrays as surface data.
Eventually I found a quick method involving rendering the final image to a string of encoded
color values, which pygame accepts.

I even resorted to unrolling a couple loops in an attempt to speed up hot code.

## Running

` $ python main.py`

Required:
+ Python 2.7
+ PyGame 1.9.1
+ Numpy 1.8.2

## Font

The GUI uses a TrueType version of Hugo Chargois's [Gohu-Font](http://font.gohu.org/).
