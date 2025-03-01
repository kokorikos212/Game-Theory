# Game-Theory

### Consider the Normal-Form Game Between Four Players

Consider the normal-form game involving four players {1, 2, 3, 4}. The number of strategies available to each player depends on your student ID number (AM) as follows:  

- Player 1 has as many strategy choices as the 1st digit of the AM.  
- Player 2 has as many strategy choices as the 2nd digit of the AM.  
- Player 3 has as many strategy choices as the 3rd digit of the AM.  
- Player 4 has as many strategy choices as the 4th digit of the AM.  

Additionally, a constant number \( c > 20 \) is added to each of these sets.  
For example, if the AM is 1234 and \( c = 20 \), then:  

$$
S_1 = \{s_1, \dots, s_{21} \}
$$  

$$
S_2 = \{s_1, \dots, s_{22} \}
$$  

$$
S_3 = \{s_1, \dots, s_{23} \}
$$  

$$
S_4 = \{s_1, \dots, s_{24} \}
$$  

The payoff functions for each player are:

$$
u_1 (s_i , s_j , s_k , s_\ell ) = 10 - i + j + 2k - 3\ell
$$

$$
u_2 (s_i , s_j , s_k , s_\ell ) = 8 + i - j + k + 4\ell
$$

$$
u_3 (s_i , s_j , s_k , s_\ell ) = 5 + 2i - j + 3k - \ell
$$

$$
u_4 (s_i , s_j , s_k , s_\ell ) = 7 - i + j - k + 2\ell
$$

where:  

$$
i \in \{1, \dots, |S_1| \}
$$  

$$
j \in \{1, \dots, |S_2| \}
$$  

$$
k \in \{1, \dots, |S_3| \}
$$  

$$
\ell \in \{1, \dots, |S_4| \}
$$  

Use a programming language of your choice to implement the following solution concepts:  

- **IESDS** (Iterated Elimination of Strictly Dominated Strategies)  
- **IEWDS** (Iterated Elimination of Weakly Dominated Strategies)  
- **IENBR** (Iterated Elimination of Never-Best Responses)  

**Which strategies survive in each case?**
