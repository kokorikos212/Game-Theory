## Game Description

Two players each choose a positive integer from the set  
&nbsp;&nbsp;&nbsp;&nbsp;**{1, 2, ..., n}**, with **n ≫ 1** (n is very large).

- If the two numbers are equal, no money is exchanged.
- If the chosen numbers differ by **1**, the player who chose the smaller number pays **1 euro** to the opponent.
- If the difference is **2 or more**, the player who chose the larger number pays **2 euros** to the opponent.

## Task

Model this game as an appropriate **linear programming (LP)** problem.  
Then:

1. Use **dominance** to simplify the strategy sets if possible.
2. Apply **off-the-shelf LP solvers** to find:
   - The **solution** to the linear programs.
   - The **common security level** (value) of the game.

## Notes

- This is a **zero-sum game**, and can be analyzed using **matrix game** techniques.
- After modeling, use LP duality to find optimal **mixed strategies** for both players.
