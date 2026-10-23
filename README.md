# Wordle 67 solver

## Intro

Hi, I'm lol1022

Played Wordle with friends in a Discord server for a while.<br>
A friend of mine saw a post that someone made 67 in it,<br>
so he decided to copy that and try it in the sever.<br>
Another friend of mine is kinda annoyed of it (the good way) cause it stayed there for a whole day or so.<br>
We found it pretty funny thus the code is born.

I know someone out there must have done it before<br>
but I decided to build one just for fun

## Basics

This is a script to generate 67 pattern inside wordle

By typing in your word<br>
the code will try to generate the first word that match the color needed in alphabetic order

there are now 6 patterns included

pattern_67_0<br>
🟩🟩🟩⬜⬜<br>
🟩⬜🟨🟨🟨<br>
🟩🟩🟩⬜🟨<br>
🟩⬜🟩⬜🟨<br>
🟩🟩🟩⬜🟨<br>
⬜⬜⬜⬜🟨<br>

pattern_67_1<br>
🟨🟨🟨⬜⬜<br>
🟨⬜🟩🟩🟩<br>
🟨🟨🟨⬜🟩<br>
🟨⬜🟨⬜🟩<br>
🟨🟨🟨⬜🟩<br>
⬜⬜⬜⬜🟩<br>

pattern_67_2<br>
⬜⬜🟩🟩🟩<br>
🟩🟩🟩⬜🟩<br>
🟩⬜⬜⬜🟩<br>
🟩🟩🟩⬜🟩<br>
🟩⬜🟩⬜🟩<br>
🟩🟩🟩⬜⬜<br>

pattern_67_3<br>
⬜⬜🟨🟨🟨<br>
🟨🟨🟨⬜🟨<br>
🟨⬜⬜⬜🟨<br>
🟨🟨🟨⬜🟨<br>
🟨⬜🟨⬜🟨<br>
🟨🟨🟨⬜⬜<br>

pattern_67_4<br>
⬜⬜🟨🟨🟨<br>
🟩🟩🟩⬜🟨<br>
🟩⬜⬜⬜🟨<br>
🟩🟩🟩⬜🟨<br>
🟩⬜🟩⬜🟨<br>
🟩🟩🟩⬜⬜<br>

pattern_67_5<br>
⬜⬜🟩🟩🟩<br>
🟨🟨🟨⬜🟩<br>
🟨⬜⬜⬜🟩<br>
🟨🟨🟨⬜🟩<br>
🟨⬜🟨⬜🟩<br>
🟨🟨🟨⬜⬜<br>

(pattern 0 and 1 have no same color version cause it might look like 87)<br>
🟩🟩🟩⬜⬜<br>
🟩⬜🟩🟩🟩<br>
🟩🟩🟩⬜🟩<br>
🟩⬜🟩⬜🟩<br>
🟩🟩🟩⬜🟩<br>
⬜⬜⬜⬜🟩<br>

As the code will run thorugh all of the pattern<br>
some of them (or all of them, I hope not) might not be achievable<br>
sometimes it needs words that not exits or implimented to fulfill the space

When entering targeted answer, the code only checks if it is 5 letters<br>
so words such as "1a2bc" will still count as a valid input<br>
upper and lower cases doesn't matter as it will auto adjust

Results will be shown as the following

['ideal', [1, 0, 0, 0, 2]]<br>
pattern ? failed

first is the word to be input in-game<br>
second is the expected color<br>
0 = gray, 1 = yellow, 2 = green<br>
the last line will show whether pattern is achievable

The window should stay opened unitl Enter is pressed(making an input)

## Result Example

### Success

ERUPT (Wordle #1000)

Answer (5 letters) = ERUPT<br>
['erugo', [2, 2, 2, 0, 0]]<br>
['equip', [2, 0, 2, 0, 1]]<br>
['abamp', [0, 0, 0, 0, 1]]<br>
pattern 0 failed

['perae', [1, 1, 1, 0, 0]]<br>
['perst', [1, 1, 1, 0, 2]]<br>
['pleat', [1, 0, 1, 0, 2]]<br>
['perst', [1, 1, 1, 0, 2]]<br>
['abaft', [0, 0, 0, 0, 2]]<br>
pattern 1 failed

['poupt', [0, 0, 2, 2, 2]]<br>
['eruct', [2, 2, 2, 0, 2]]<br>
['ebbet', [2, 0, 0, 0, 2]]<br>
['eruct', [2, 2, 2, 0, 2]]<br>
['educt', [2, 0, 2, 0, 2]]<br>
['erugo', [2, 2, 2, 0, 0]]<br>
pattern 2 success

['after', [0, 0, 1, 1, 1]]<br>
['perdu', [1, 1, 1, 0, 1]]<br>
['padle', [1, 0, 0, 0, 1]]<br>
['perdu', [1, 1, 1, 0, 1]]<br>
['parae', [1, 0, 1, 0, 1]]<br>
['perae', [1, 1, 1, 0, 0]]<br>
pattern 3 success

['after', [0, 0, 1, 1, 1]]<br>
['eager', [2, 0, 0, 0, 1]]<br>
['equip', [2, 0, 2, 0, 1]]<br>
['erugo', [2, 2, 2, 0, 0]]<br>
pattern 4 failed

['poupt', [0, 0, 2, 2, 2]]<br>
['perst', [1, 1, 1, 0, 2]]<br>
['pahit', [1, 0, 0, 0, 2]]<br>
['perst', [1, 1, 1, 0, 2]]<br>
['pleat', [1, 0, 1, 0, 2]]<br>
['perae', [1, 1, 1, 0, 0]]<br>
pattern 5 success

Press Enter to exit...

### Failed

KAYAK (Wordle 671)

Answer (5 letters) = KAYAK<br>
['kayle', [2, 2, 2, 0, 0]]<br>
['khaya', [2, 0, 1, 1, 1]]<br>
['beefy', [0, 0, 0, 0, 1]]<br>
pattern 0 failed

['akara', [1, 1, 1, 0, 0]]<br>
['aback', [1, 0, 1, 0, 2]]<br>
['blink', [0, 0, 0, 0, 2]]<br>
pattern 1 failed

['kiosk', [2, 0, 0, 0, 2]]<br>
['kayle', [2, 2, 2, 0, 0]]<br>
pattern 2 failed

['beaky', [0, 0, 1, 1, 1]]<br>
['abbey', [1, 0, 0, 0, 1]]<br>
['agamy', [1, 0, 1, 0, 1]]<br>
['akara', [1, 1, 1, 0, 0]]<br>
pattern 3 failed

['beaky', [0, 0, 1, 1, 1]]<br>
['kedgy', [2, 0, 0, 0, 1]]<br>
['kayle', [2, 2, 2, 0, 0]]<br>
pattern 4 failed

['acock', [1, 0, 0, 0, 2]]<br>
['aback', [1, 0, 1, 0, 2]]<br>
['akara', [1, 1, 1, 0, 0]]<br>
pattern 5 failed

Press Enter to exit...<br>

## Special Thanks

The word list is cited from @cfreshman

[nyt-wordle-allowed-guesses-2026-03-06.txt](https://gist.github.com/cfreshman/8b92bc418b43096094cf5d1b0eea8f84)<br>
NYT Wordle allowed guesses as of 2026-03-06<br>
at Github by cfreshman

and also, 67
