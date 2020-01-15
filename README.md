# Starnavi Test Task

**Treasure Hunt**

34 21 32 41 25
14 42 43 14 31
54 45 52 42 23
33 15 51 31 35
21 52 33 13 23

You need to write a program to explore the above table for a treasure. 

The values in the table are clues. Each cell contains a number between 11 and 55, where the ten’s
digit represents the row number and the unit’s digit represents the column number of the cell
containing the next clue. Starting with the upper left corner (at 1,1), use the clues to guide your
search through the table. The treasure is a cell whose value is the same as its coordinates.
Your program must first read in the treasure map data into a 5 by 5 array.

**Implementation**

Write two different implementations. The first should use a functional programming approach
(closures, native data structures). The second implementation should be implemented in an
object-oriented way (object models, simple OO patterns). One of the implementations should be
coded with recursion, the other without recursion. To every implementation you need to create unit
test. For creating unit test we are suggests using pytest.

**Example of input**

55 14 25 52 21
44 31 11 53 43
24 13 45 12 34
42 22 43 32 41
51 23 33 54 15

**Example of output**

11 55 15 21 44 32 13 25 43

## To run locally

Install dependencies with [Poetry](https://python-poetry.org/docs/):
```python
poetry install
```
To run FP implementation:
```python
python run.py --implementation fp
```

To run OOP implementation:
```python
python run.py --implementation oop
python run.py  # It uses OOP implementation by default.

```
To run tests:
```python
python -m pytest
```

