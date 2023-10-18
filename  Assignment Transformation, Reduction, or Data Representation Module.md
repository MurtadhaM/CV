
## Assignment: Transformation, Reduction, or Data Representation Module

<p align="center">
<img src="https://avatars.githubusercontent.com/u/45076915?s=200&v=4" width=20%/>
</p>
<p align="center">  
<img src="https://img.shields.io/badge/Author-Murtadha Marzouq-blue" width=20%/>
</p>

---

#### $\color{red}{\text{1.}}$ You are given a collection of n bolts of different widths and n corresponding nuts. You are allowed to try a nut and bolt together, from which you can determine whether the nut is larger than the bolt, smaller than the bolt, or matches the bolt exactly. However, there is no way to compare two nuts together or two bolts together. The problem is to match each bolt to its nut. 



$\boxed{\color{red}\text{Design an algorithm for this problem with average-case efficiency in  ({n} log {n}).}}$ 
#### $\color{green}{\text{Pseudocode}}$

```python
1.  Let A be an array of n bolts and B be an array of n nuts.
2.  If n = 1, then return the pair (A[1], B[1]).
3.  Pick a random bolt A[i] and partition B into three sets: 
    B1 = {nuts smaller than A[i]}, B2 = {nuts larger than A[i]}, and B3 = {nuts matching A[i]}.
4.  Partition A into three sets: A1 = {bolts smaller than B[i]}, A2 = {bolts larger than B[i]}, and A3 = {bolts matching B[i]}.
5.  Recursively match the pairs in A1 and B1, and the pairs in A2 and B2.
6.  Return the pair (A[i], B[i]).    
```

#### $\color{green}{\text{Analysis and Explaination}} $

The algorithm partitions the nuts and bolts into three sets of equal size, and then recursively matches the pairs in the two smaller sets. The algorithm runs in time O(n) to partition the nuts and bolts, and the two recursive calls each run in time T(n/3). The total running time is therefore T(n) = O(n) + 2T(n/3). By the master theorem, the running time is O(n log n).

--- 


#### $\color{red}{\text{2.}}$ Image a handful of uncooked spaghetti, individual rods whose lengths represent numbers that need to be sorted.  Outline a sorting algorithm that takes advantage of this unorthodox representation.

---

${\color{green}\text{The Algorithm that would look similar to the following:}}$

```python
def spaghetti_sort(arr):
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(n - 1):
            # Compare the lengths of two spaghetti rods
            if arr[i] > arr[i + 1]:
                # Swap the positions of the spaghetti rods
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
    return ar
```

#### $\color{green}{\text{Analysis and Explaination}} $

The algorithm is similar to quicksort, but instead of partitioning the array into two parts, it partitions the array into three parts. The algorithm picks a random element x from the array and partitions the array into three sets: A1 = {elements smaller than x}, A2 = {elements equal to x}, and A3 = {elements larger than x}. The algorithm then recursively sorts A1 and A3, and returns the concatenation of the three sorted arrays. The algorithm runs in time O(n) to partition the array, and the two recursive calls each run in time T(n/3). The total running time is therefore T(n) = O(n) + 2T(n/3). By the master theorem, the running time is O(n log n).

##### $\textcolor{red}{Note:}$ I do not fully understand the question, but I tried to answer it as best I could and I hope it is correct.

----

#### $\color{red}{\text{3.}}$  A peasant finds himself on a river bank with a wolf, a goat, and a head of cabbage. He needs to transport all three to the other side of the river in his boat. He needs to transport all three to the other side of the river in his boat. However, the boat has room only for the peasant himself and one other item (either the wolf, the goat, or the cabbage). In his absence, the wolf would eat the goat, and the goat would eat the cabbage. Could you find a way for the peasant to solve this problem or prove that it has no solution?

#### $\color{green}{\text{Solution:}} $

1. $\color{red}{\text{The peasant takes the goat across the river.}}$
2. $\color{red}{\text{The peasant returns alone.}}$
3. $\color{red}{\text{The peasant takes the cabbage across the river.}}$
4. $\color{red}{\text{The peasant returns with the goat.}}$
5. $\color{red}{\text{The peasant takes the wolf across the river.}}$
6. $\color{red}{\text{The peasant returns alone.}}$


#### ${\color{green}\text{Demostration of the solution}}$

<!--
| Trip | Left Bank | River | Right Bank | Action |
| :---: | :---: | :---: | :---: | :---: |
| 1 | <img src=https://i.pinimg.com/736x/d7/4a/9f/d74a9f40c8adc8cae77d7dfe428b74db.jpg width=50px>,  <img src=https://static.vecteezy.com/system/resources/previews/023/546/329/original/enhancing-your-designs-with-a-transparent-cartoon-goat-free-png.png width=50px> , <img src=https://i.pinimg.com/originals/02/50/54/0250548df2b4e968a7e92d7f68f353cb.png width=50px> | | | |
| 2 | <img src=https://i.pinimg.com/736x/d7/4a/9f/d74a9f40c8adc8cae77d7dfe428b74db.jpg width=50px>, <img src=https://i.pinimg.com/originals/02/50/54/0250548df2b4e968a7e92d7f68f353cb.png width=50px> | |  <img src=https://static.vecteezy.com/system/resources/previews/023/546/329/original/enhancing-your-designs-with-a-transparent-cartoon-goat-free-png.png width=50px>  | Peasant takes the Goat across the river |
| 3 | <img src=https://i.pinimg.com/736x/d7/4a/9f/d74a9f40c8adc8cae77d7dfe428b74db.jpg width=50px>, <img src=https://i.pinimg.com/originals/02/50/54/0250548df2b4e968a7e92d7f68f353cb.png width=50px> | |  <img src=https://static.vecteezy.com/system/resources/previews/023/546/329/original/enhancing-your-designs-with-a-transparent-cartoon-goat-free-png.png width=50px>  | Peasant returns alone |
| 4 | <img src=https://i.pinimg.com/736x/d7/4a/9f/d74a9f40c8adc8cae77d7dfe428b74db.jpg width=50px> | |  <img src=https://static.vecteezy.com/system/resources/previews/023/546/329/original/enhancing-your-designs-with-a-transparent-cartoon-goat-free-png.png width=50px> , <img src=https://i.pinimg.com/originals/02/50/54/0250548df2b4e968a7e92d7f68f353cb.png width=50px> | Peasant takes the  Cabbage  across the river |
| 5 | <img src=https://i.pinimg.com/736x/d7/4a/9f/d74a9f40c8adc8cae77d7dfe428b74db.jpg width=50px>,  <img src=https://static.vecteezy.com/system/resources/previews/023/546/329/original/enhancing-your-designs-with-a-transparent-cartoon-goat-free-png.png width=50px>  | | <img src=https://i.pinimg.com/originals/02/50/54/0250548df2b4e968a7e92d7f68f353cb.png width=50px> | Peasant returns with the  Goat || 6 |  <img src=https://static.vecteezy.com/system/resources/previews/023/546/329/original/enhancing-your-designs-with-a-transparent-cartoon-goat-free-png.png width=50px>  | | <img src=https://i.pinimg.com/736x/d7/4a/9f/d74a9f40c8adc8cae77d7dfe428b74db.jpg width=50px>, <img src=https://i.pinimg.com/originals/02/50/54/0250548df2b4e968a7e92d7f68f353cb.png width=50px> | Peasant takes the Cabbage across the river |
| 7 |  <img src=https://static.vecteezy.com/system/resources/previews/023/546/329/original/enhancing-your-designs-with-a-transparent-cartoon-goat-free-png.png width=50px>  | | <img src=https://i.pinimg.com/736x/d7/4a/9f/d74a9f40c8adc8cae77d7dfe428b74db.jpg width=50px>, <img src=https://i.pinimg.com/originals/02/50/54/0250548df2b4e968a7e92d7f68f353cb.png width=50px> | Peasant returns alone |
| 8 | | | <img src=https://i.pinimg.com/736x/d7/4a/9f/d74a9f40c8adc8cae77d7dfe428b74db.jpg width=50px>,  <img src=https://static.vecteezy.com/system/resources/previews/023/546/329/original/enhancing-your-designs-with-a-transparent-cartoon-goat-free-png.png width=50px> , <img src=https://i.pinimg.com/originals/02/50/54/0250548df2b4e968a7e92d7f68f353cb.png width=50px> | Peasant takes the goat across the river | 
-->
<p align=center> <img src=image-1.png width=1000%></p>
---
 
#### $\color{red}{\text{4.}}$ Consider the two-dimensional post office location problem: given n points (x1, y1),......, (xn, yn) in the Cartesian plane, find a location (x, y) for a post office that minimizes ,t$\frac{1}{n}\sum^n_{i=1}\:\left(\left|x_i\:-x\right|\:+\:\left|y_i\:-\:y\right|\right)$ he average Manhattan distance from the post office to these points. Explain how this problem can be efficiently solved by the problem reduction technique, provided the post office does not have to be located at one of the input points.


#### $\color{green}{\text{Justification:}} $

$\color{red}{\text{The problem can be solved by finding the median of the x-coordinates and the median of the y-coordinates.}}$

*This method eliminates the need for complex iterative optimization algorithms, as finding the medians can be done in linear time, making it an efficient approach. It should be noted that this solution works when the post office is not constrained to be at one of the input points.*

$\color{blue}{\text{Reference: Lecture Slides}}$
<p align=center> <img src=image.png width=70%></p>

###### $\color{red}{Note:}$*$\color{orange}\text{I am taking Computer Vision this semester and I have learned about similar problems.}$*
 ---
