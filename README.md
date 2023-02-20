# TikTacToe with MinMax AI

## MinMax Algorithm

The MinMax algorithm is a decision-making algorithm commonly used in game theory and AI. It works by recursively exploring all possible moves and their outcomes, assuming that the opponent will make the best move for their own interests. The algorithm alternates between maximizing the player's score (the "Max" step) and minimizing the opponent's score (the "Min" step), hence the name "MinMax".

In the context of TicTacToe, the MinMax algorithm is used to determine the best move for the AI player, assuming that the human player will make the best possible move for their own interests. By exploring all possible moves and outcomes, the algorithm can guarantee that it will never lose, and in some cases, it can even win the game.

## Alpha-Beta Pruning

One issue with MinMax is that it can be very computationally expensive, especially for games with a large number of possible moves. To address this issue, the alpha-beta pruning technique can be used to eliminate unnecessary branches of the search tree.

The idea behind alpha-beta pruning is to keep track of the best possible scores found so far for both the Max and Min steps, and prune any branches that are guaranteed to not lead to a better outcome. This can significantly reduce the number of nodes explored by the MinMax algorithm, making it more efficient.

In this project, I implemented the alpha-beta pruning technique to speed up the MinMax algorithm and make the TicTacToe game more responsive.

## Acknowledgements

I am extremely grateful to the CS50 team for creating such an excellent course and providing me with the opportunity to learn about AI and game theory. The course has not only taught me about the technical details of these subjects, but also their broader applications and implications. I highly recommend it to anyone interested in these fields.
