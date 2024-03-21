# Kata_TICTACTOE
### Code by: Fernando A. Rodriguez
---

[Live Coding on Youtube](https://www.youtube.com/playlist?list=PLxFn4mrvRfPU6FJ2JYunNMw-Ybpz1Ma6I)

Para correr el programa solo es necesario  escribir `python "nombre del programa"`, solo es necesario instalar [python](https://www.python.org/downloads/) caso de no tenerlo instalado 

---

## Kata diary

### Kata session 01:

In the first session of the kata we carried out the exercise using if conditionals to verify each of the possible scenarios in which a player could win, however, there was the problem that the problem was that using the program could only make plays sequentially having to use square number one then square number two and so on until the end of the game.

### Kata session 02:

During the kata 02 session, an attempt was made to correct the problem of having to play sequentially and in this way the player can play freely on the square they want, however when trying to implement the game logic and solve the bug that You could only play sequentially, I got a little stuck since I wasn't seeing the whole picture and the logic wasn't implemented in an efficient way, at one point I realized that I would have to use two arrangements, in which the first would be for the board and the second to store positions or plays.

### Kata session 03:

At the time of performing Kata 03, I made the decision to use the initial logic, I began by implementing each of the corresponding logics for the first player, which were the same ones that I used in the kata 01 session, then I implemented a counter for the first player. while loop to define the number of maximum plays and then a boolean to alternate between player one and player two, once the game logic was implemented and the ability to alternate between players, it was only necessary to define a variable called "select_position" which then If the user receives a value, -1 will be subtracted to match the position selected by the user with the position of the arrangement and the letter of the corresponding player (X or Y) will automatically be inserted.
