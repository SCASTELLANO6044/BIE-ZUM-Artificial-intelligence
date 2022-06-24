# N queens problem.

We observe that a valid solution can have only one queen per row, which means that we can represent the board as an array of eight elements, where each entry represents the column position of the queen from a particular row.

Queens position can be represented as the occupied positions of a two dimensional array: [0, 6], [1, 2], [2, 7], [3, 1], [4, 4], [5, 0], [6, 5], [7, 3], but as we know on each row there is going to be one queen, we can reprensent it on a one dimensional elements array: [6, 2, 7, 1, 4, 0, 5, 3].

If we look closely at the example solution [6, 2, 7, 1, 4, 0, 5, 3], we note that a potential solution to the eight queens puzzle can be constructed by generating all possible permutations of an array of eight numbers, [0, 1, 2, 3, 4, 5, 6, 7], and rejecting the invalid states (the ones in which any two queens can attack each other).

My implementation uses a recursive approach: assume that we’ve already generated all possible ways to place *k* queens on the first *k* rows. In order to generate the valid positions for the *k+1* queen we place a queen on all columns of row *k+1* and we reject the invalid states. We do the above steps until all eight queens are placed on the board.
