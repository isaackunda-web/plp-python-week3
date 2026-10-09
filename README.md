# PLP Python Week 3 Assignment: Conditions and Loops

This repository contains solutions for the Week 3 assignment covering conditional decision-making (`if`/`elif`/`else`) and iterative processing with loops (`for` and `while`) in Python.

## File Descriptions

- **`grade_reporter.py`**: Reads a list of test scores, assigns letter grades (A, B, C, F), counts passing and failing students, and computes the class average.
- **`bug_hunt.py`**: A debugged Python script that correctly calculates the sum of numbers from 1 to 5 (`15`) using a `while` loop.

## Reflection Questions

The hardest bug to locate in Part B was the **logic bug** (`while count < 5`), because unlike syntax or type errors, Python executed the script without throwing any error message. I knew something was wrong because the program outputted `10` instead of the expected mathematical sum of `15` ($1 + 2 + 3 + 4 + 5 = 15$). Trace-debugging the loop revealed that the loop condition terminated before `count` reached `5`, which required changing the condition to `count <= 5`.