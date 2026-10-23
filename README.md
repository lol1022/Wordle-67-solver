# Wordle 67 solver

## Intro

Hi, I'm lol1022

Played Wordle with friends in a Discord server for a while.
A friend of mine saw a post that someone made 67 in it,
so he decided to copy that and try it in the sever.
Another friend of mine is kinda annoyed of it (the good way) cause it stayed there for a whole day or so.
We found it pretty funny thus the code is born.

I know someone out there must have done it before
but I decided to build one just for fun

## Basics

This is a script to generate 67 pattern inside wordle

By typing in your word
the code will try to generate the first word that match the color needed in alphabetic order

there are now 6 patterns included

pattern_67_0
🟩🟩🟩⬜⬜
🟩⬜🟨🟨🟨
🟩🟩🟩⬜🟨
🟩⬜🟩⬜🟨
🟩🟩🟩⬜🟨
⬜⬜⬜⬜🟨

pattern_67_1
🟨🟨🟨⬜⬜
🟨⬜🟩🟩🟩
🟨🟨🟨⬜🟩
🟨⬜🟨⬜🟩
🟨🟨🟨⬜🟩
⬜⬜⬜⬜🟩

pattern_67_2
⬜⬜🟩🟩🟩
🟩🟩🟩⬜🟩
🟩⬜⬜⬜🟩
🟩🟩🟩⬜🟩
🟩⬜🟩⬜🟩
🟩🟩🟩⬜⬜

pattern_67_3
⬜⬜🟨🟨🟨
🟨🟨🟨⬜🟨
🟨⬜⬜⬜🟨
🟨🟨🟨⬜🟨
🟨⬜🟨⬜🟨
🟨🟨🟨⬜⬜

pattern_67_4
⬜⬜🟨🟨🟨
🟩🟩🟩⬜🟨
🟩⬜⬜⬜🟨
🟩🟩🟩⬜🟨
🟩⬜🟩⬜🟨
🟩🟩🟩⬜⬜

pattern_67_5
⬜⬜🟩🟩🟩
🟨🟨🟨⬜🟩
🟨⬜⬜⬜🟩
🟨🟨🟨⬜🟩
🟨⬜🟨⬜🟩
🟨🟨🟨⬜⬜

(pattern 0 and 1 have no same color version cause it might look like 87)
🟩🟩🟩⬜⬜
🟩⬜🟩🟩🟩
🟩🟩🟩⬜🟩
🟩⬜🟩⬜🟩
🟩🟩🟩⬜🟩
⬜⬜⬜⬜🟩

As the code will run thorugh all of the pattern
some of them (or all of them, I hope not) might not be achievable
sometimes it needs words that not exits or implimented to fulfill the space

When entering targeted answer, the code only checks if it is 5 letters
so words such as "1a2bc" will still count as a valid input
upper and lower cases doesn't matter as it will auto adjust

Results will be shown as the following

['ideal', [1, 0, 0, 0, 2]]
pattern ? failed

first is the word to be input in-game
second is the expected color
0 = gray, 1 = yellow, 2 = green
the last line will show whether pattern is achievable

The window should stay opened unitl Enter is pressed(making an input)

## Result Example

### Success

ERUPT (Wordle #1000)

Answer (5 letters) = ERUPT
['erugo', [2, 2, 2, 0, 0]]
['equip', [2, 0, 2, 0, 1]]
['abamp', [0, 0, 0, 0, 1]]
pattern 0 failed

['perae', [1, 1, 1, 0, 0]]
['perst', [1, 1, 1, 0, 2]]
['pleat', [1, 0, 1, 0, 2]]
['perst', [1, 1, 1, 0, 2]]
['abaft', [0, 0, 0, 0, 2]]
pattern 1 failed

['poupt', [0, 0, 2, 2, 2]]
['eruct', [2, 2, 2, 0, 2]]
['ebbet', [2, 0, 0, 0, 2]]
['eruct', [2, 2, 2, 0, 2]]
['educt', [2, 0, 2, 0, 2]]
['erugo', [2, 2, 2, 0, 0]]
pattern 2 success

['after', [0, 0, 1, 1, 1]]
['perdu', [1, 1, 1, 0, 1]]
['padle', [1, 0, 0, 0, 1]]
['perdu', [1, 1, 1, 0, 1]]
['parae', [1, 0, 1, 0, 1]]
['perae', [1, 1, 1, 0, 0]]
pattern 3 success

['after', [0, 0, 1, 1, 1]]
['eager', [2, 0, 0, 0, 1]]
['equip', [2, 0, 2, 0, 1]]
['erugo', [2, 2, 2, 0, 0]]
pattern 4 failed

['poupt', [0, 0, 2, 2, 2]]
['perst', [1, 1, 1, 0, 2]]
['pahit', [1, 0, 0, 0, 2]]
['perst', [1, 1, 1, 0, 2]]
['pleat', [1, 0, 1, 0, 2]]
['perae', [1, 1, 1, 0, 0]]
pattern 5 success

Press Enter to exit...

### Failed

KAYAK (Wordle 671)

Answer (5 letters) = KAYAK
['kayle', [2, 2, 2, 0, 0]]
['khaya', [2, 0, 1, 1, 1]]
['beefy', [0, 0, 0, 0, 1]]
pattern 0 failed

['akara', [1, 1, 1, 0, 0]]
['aback', [1, 0, 1, 0, 2]]
['blink', [0, 0, 0, 0, 2]]
pattern 1 failed

['kiosk', [2, 0, 0, 0, 2]]
['kayle', [2, 2, 2, 0, 0]]
pattern 2 failed

['beaky', [0, 0, 1, 1, 1]]
['abbey', [1, 0, 0, 0, 1]]
['agamy', [1, 0, 1, 0, 1]]
['akara', [1, 1, 1, 0, 0]]
pattern 3 failed

['beaky', [0, 0, 1, 1, 1]]
['kedgy', [2, 0, 0, 0, 1]]
['kayle', [2, 2, 2, 0, 0]]
pattern 4 failed

['acock', [1, 0, 0, 0, 2]]
['aback', [1, 0, 1, 0, 2]]
['akara', [1, 1, 1, 0, 0]]
pattern 5 failed

Press Enter to exit...

## Special Thanks

The word list is cited from @cfreshman

[nyt-wordle-allowed-guesses-2026-03-06.txt](https://gist.github.com/cfreshman/8b92bc418b43096094cf5d1b0eea8f84)
NYT Wordle allowed guesses as of 2026-03-06
at Github by cfreshman

and also, 67
