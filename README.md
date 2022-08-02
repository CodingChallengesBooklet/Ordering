# Ordering
In this code challenge we create a program that sort a list of integers into ascending or descending order.

![GitHub followers](https://img.shields.io/github/followers/hrszpuk?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/hrszpuk?style=social)
<br>
![GitHub language count](https://img.shields.io/github/languages/count/CodingChallengesBooklet/Ordering?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/CodingChallengesBooklet/Ordering?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/CodingChallengesBooklet/Ordering?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/CodingChallengesBooklet/Ordering?style=for-the-badge)
![GitHub branch checks state](https://img.shields.io/github/checks-status/CodingChallengesBooklet/Ordering/main?style=for-the-badge)

## Problem
Create a program that allows entry of 10 numbers and then sorts them into ascending or descending order, based on user input

### Extension problems
1. The user can input a word or string, and it arranges the string into alphabetical order. E.g. My Rabbit would be shown as “abbimty “. (Punctuation placement is not essential)
2. Repeat Extension 1, but include the sentence structure

## Solution
Many languages have built-in sorting libraries or methods, such as with Python which has a `sorted()` function to sort lists easily.
However, some languages do not have these features, and so, the pseudocode here uses a very simple algorithm to sort into descending and ascending order.
The algorithm loops over the list, gets the biggest number in the list, removes it from the list, and adds it to a new list.
Since the biggest number is removed everytime, we will get the next biggest number on every loop through the list.
Adding the biggest to a new list would mean the biggest numbers are first in the list and the smallest are last.
*NOTE: for ascending this is the same but with the smallest number everytime instead of the biggest.*

So to get started, we create and empty list to store our ten numbers then get an input 10 times and add each number to our list of numbers.
These will be the numbers we are going to sort.
```python
numbers = EMPTY LIST

LOOP 10 TIMES
    number = INPUT
    ADD number TO numbers
END
```
Next, we are going to sort these numbers into descending order.
We do this by looping 10 times. 
Getting the biggest number every loop, adding the number to our list `descending_numbers` and removing this number from `numbers`.
```python
descending_numbers = EMPTY_LIST
LOOP 10 TIMES
    biggest = GET BIGGEST IN numbers
    ADD biggest TO descending_numbers
    REMOVE biggest FROM numbers
END
```
Below is the same code but for ascending order. This code is exactly the same but we need to get the smallest instead of the biggest.
```python
ascending_numbers = EMPTY_LIST
LOOP 10 TIMES
    smallest = GET SMALLEST IN numbers
    ADD smallest TO descending_numbers
    REMOVE smallest FROM numbers
END
```
Finally, we can output the new sorted lists to the user.
```python
OUTPUT descending_numbers
OUTPUT ascending_numbers
```
    
