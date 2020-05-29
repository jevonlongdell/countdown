#! /usr/bin/python3

target = int(input("Enter target > "))
numbers = list(map(int, input(
    "Enter numbers separated by white space > ").split()))

numbers.sort(reverse=True)


def apply_postfix(expr):
    # This implements a RPN calculator, turning a
    # RPN expression in a stack of numbers
    if len(expr) == 0:
        return []
    g = expr.copy()
    g.reverse()
    st = []
    while len(g) != 0:
        x = g.pop()
        if x == "+":
            st.append(st.pop() + st.pop())
        elif x == "-":
            st.append( - st.pop() + st.pop())
        elif x == "*":
            st.append(st.pop() * st.pop())
        else:
            st.append(x)
    return st


# Has a solution been found
solutionfound = False

# Has a solution been found that uses
# all the numbers
solutionfound_allnum = False

# What's the closest we've got
closest = 0
closest_expression = []


def itit(expr, numbersleft):
    # This is the function we call iteratively to try
    # all the different possible expressions
    global solutionfound
    global solutionfound_allnum
    global closest
    global closest_expression
    if solutionfound_allnum:
        return # We're all done
    st = apply_postfix(expr)
    if len(st) == 1:
        if not solutionfound:
            if st[0] == target:
                print("Found solution")
                print(expr)
                print(target)
                solutionfound = True
        if not solutionfound_allnum and numbersleft == []:
            if st[0] == target:
                print("Found solution with all numbers")
                print(expr)
                print(target)
                solutionfound_allnum = True
                return
        if abs(st[0]-target) < abs(target-closest):
            closest = st[0]
            closest_expression = expr.copy()

    # Can we add an operator to the end?
    # If so explore all the different options
    # with a +,-,* appended to the current expression

    if len(st) >= 2:
        newexpr = expr.copy()
        newexpr.append("+")
        itit(newexpr, numbersleft)
        newexpr = expr.copy()
        newexpr.append("-")
        itit(newexpr, numbersleft)
        newexpr = expr.copy()
        newexpr.append("*")
        itit(newexpr, numbersleft)

    # try adding each of the numbers left to each
    # current expression
    for (i, x) in enumerate(numbersleft):
        newexpr = expr.copy()
        newexpr.append(x)
        newnumbersleft = numbersleft.copy()
        newnumbersleft.pop(i)
        itit(newexpr, newnumbersleft)


itit([], numbers)


if not solutionfound:
    print("Closest I could find was:")
    print(closest_expression)
    print(closest)
