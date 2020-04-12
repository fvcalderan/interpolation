# Interpolation

Generate simple plots and Lagrange Polynomials for interpolations of given sets of points.

See https://en.wikipedia.org/wiki/Lagrange_polynomial for reference on what those polynomials are.

### Usage

This program receives a `.csv` file as input, which contains two columns (`x` and `y`). Each row represents a point in `(x, y)`. See example_data.csv.

Also, a precision value needs to be passed to the program, so it knows the "resolution" of the interpolation. For example: a precision of `0.1` will generate interpolated points every `0.1` units in the `x` axis.

Finally, an output name needs to be given. The program will generate two files: [outputname]_LaTeX.txt and [outputname].png. The first file will contain the code to represent the polynomial in a LaTeX document and the second is a plot.

In other words: `python3 interpolation.py data.csv precision output_name`.
