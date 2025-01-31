# Exercise: Coordinate Geometry

In high school, you learned basic 2D coordinate geometry formulas to calculate **distance** and **slope** between two points, $(x_1, y_1)$ and $(x_2, y_2)$:

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

$$
m = \frac{y_2 - y_1}{x_2 - x_1}
$$

## Task

Create a Python program, `geometry.py`, that:

1. Prompts the user for four values: $x_1, y_1, x_2,$ and $y_2$.
2. Computes **distance** and **slope** using the formulas above.
3. Prints the results, **rounded to two decimal places**.

Your program should run **without errors** when I execute:

```shell
uv run geometry.py
```

### Example Output

```Output
For the points (4,5) and (6,7), their distance is 2.83 and the slope is 1.00.
```

### Hints

- You can use multiple `input()` lines to get $x_1, y_1, x_2,$ and $y_2$.
- `input()` returns a string, not a number.
- The `math` module has many built in functions & variables that can be of help.
- If $x_2 = x_1$, the slope formula raises a divide-by-zero error. This is expected. We’ll learn to handle such errors later. For now, assume $x_2 \neq x_1$.
