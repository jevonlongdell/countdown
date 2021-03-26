# Countdown
Solves puzzles from "Cats does Countdown" TV show

## Countdown number game
An example
```
> python3 countdown_number_game.py
Enter target > 724
Enter numbers separated by white space > 100 25 6 5 3 1
Found solution
[100, 25, '+', 5, '-', 6, '*', 3, '+', 1, '+']
724
Found solution with all numbers
[100, 25, '+', 5, '-', 6, '*', 3, '+', 1, '+']
724
```

The returned expression is in Reverse Polish Notation, that is: 
```
[100, 25, '+', 5, '-', 6, '*', 3, '+', 1, '+']
```
means

```
((100+25)-5)*6+3+1
```


## Countdown word game

An example

``` $ python3 coundown_word_game.py
Enter given letters: redcat

Given letters:
{r, e, d, c, a, t}

1 letter words:
['a', 'c', 'd', 'e', 'r', 't', 'a', 'c', 'd', 'e', 'r', 't']

2 letter words:
['ac', 'ca', 'cd', 'cr', 'ed', 'ra', 'ad', 'at', 're']

3 letter words:
['art', 'dec', 'rca', 'rae', 'red', 'tad', 'ted', 'ace', 'act', 'arc', 'are', 'art', 'ate', 'cad', 'car', 'cat', 'ear', 'eat', 'era', 'eta', 'rat', 'red', 'tad', 'tar', 'tea']

4 letter words:
['dare', 'aced', 'acre', 'card', 'care', 'cart', 'dare', 'dart', 'date', 'dear', 'race', 'rate', 'read', 'tare', 'tear']

5 letter words:
['acted', 'arced', 'cadet', 'cadre', 'cared', 'caret', 'cater', 'cedar', 'crate', 'raced', 'rated', 'react', 'recta', 'tared', 'trace', 'trade', 'tread']

6 letter words:
['carted', 'crated', 'traced']

```