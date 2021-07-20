# Faster pandas
This is the repository for the LinkedIn Learning course Faster pandas. The full course is available from [LinkedIn Learning][lil-course-url].

![Faster pandas][lil-thumbnail-url] 
Data scientists often favor pandas, because it lets them work efficiently with larger amounts of data—a useful quality as data sets become bigger and bigger. In this course, instructor Miki Tebeka shows you how to improve your pandas’ code’s speed and efficiency. First, Miki explains why performance matters and how you can measure it with Python profilers. Then, the course teaches you how to use vectorization to manipulate data. The course also walks through some common mistakes and how to address them.

Python and pandas have many high-performance built-in functions, and Miki covers how to use them. Pandas can use a lot of memory, so Miki offers good tips on how to save memory. The course demonstrates how to serialize data with SQL and HDF5. Then Miki goes over how to speed up your code with Numba and Cython. Alternative DataFrames can also speed up your code, and Miki steps through some options. Plus, explore a few extra resources that you can check out.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

## Installing
1. To use these exercise files, you must have the following installed:
	- Python 3.6 and up
	- To install packages used, run `python -m pip install -r requirements.txt` 
2. Clone this repository into your local machine using the terminal (Mac), CMD (Windows), or a GUI tool like SourceTree.
3. If you want to follow along, install [IPython](https://ipython.org/)
    - `python -m pip install ipython`

### Instructor

**Mike Tebeka**

_CEO at 353Solutions_

Check out some of my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/miki-tebeka).

[lil-course-url]: https://www.linkedin.com/learning/faster-pandas
[lil-thumbnail-url]: https://cdn.lynda.com/course/2832038/2832038-1605286392196-16x9.jpg
