---
# Quine-McCluskey
---
* Author: Ibrahima Barry
---
# Design
---
We implement a version of the Quine McCluskey algorithm for boolean algebra that
generates the minimized 2-level sum of products (SOP) and product of sums (POS) 
expressions for all single-output boolean functions with at most 10 literals. 

In this design lists, tuples, and dictionaries are the most used data
structures. The following procedure explains the algorithm: 

1. convert the minterms and "don't cares" given to binary form and group them
   based on the number of '1's' they contain. These are the '0-cubes'

2. exhaustively - accross the groups that were formed in 1. - group the 1-cubes 
   based on their hamming distance. i.e If their hamming distance is a power of 
   2 we can group them. eg) the 0-cubes 1 and 5 can be grouped together since
   ham(0001, 0101) = 4 which is a power of 2. These are the "1-cubes"

3. now from the groupings in 2. group further based on whether two 1-cubes were
   both matched with in step 2. with the same hamming distance. eg) 1-cubes (1,
   5)(4) and (9, 13)(4) both matched with a hamming distance of 4 so we can grop
   them. To form the pair write (1, 5, 9, 13)(4, 8) where (4, 8) are the minimum
   distances between any two elements in the list (1, 5, 9, 13) and the maximum
   distance, respectively. These are the "2-cubes"

4. while doing 1-3, keep track of which x-cubes were never used. These are the
   prime implicants. one can find the SOP and POS with the prime implicants, but
   it wouldn't be minimal. 

5. Next we look for prime implicants that exclusively use a minterm. i.e a
   minterm used in just a singular prime implicant. If a prime implicant has
   this property we call it an essential prime implicant and use it to generate
   the SOP and POS solution. (The details of this algorithm are long, see the 
   source (src) code)

6. Next we create a list of binaries representing our essential prime implicants. The
   process is simple: if (1, 5, 9, 13)(4, 8) is an essential prime implicant.
   Convert each number (1, 5, 9, 13) to binary and see at what indices they
   differ. At those indices put an "X" (dont-care). For this example, we get the
   string "XX01". Now we create an alphabet to represent our literals ("A, B, C, D"). 
   An "X" in the string is ignored, a '1' means logic high, and '0' means low.
   If we get a logic low append to "~" to the corresponding alphabet character.
   Here we get "~CD" as the term. The algorithm for this are in the src folder.

---
# Testing
---

Any python interpreter will work. Command line interface is prefered, especially
for file I/O. 

---
# Reflection
---
Overall, we were able to create a functioning program that minimized the logic
fully. However there are limitations as we only assumed up to 10 literals. Also,
we didnt implement functionality for x-cubes beyond x > 2 as doing 10 literals
doesn't require that many cubes. 
