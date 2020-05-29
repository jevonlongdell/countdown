# Coundown
Solves the number puzzles from the "Countdown" TV show

An example
```
> python3 countdown.py
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
```((100+25)-5)*6+3+1```
