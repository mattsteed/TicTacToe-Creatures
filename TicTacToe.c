#include <stdlib.h>
#include <stdio.h>
#include <math.h>




// print_move: Prints X if board entry is 1, O if it is -1, and blank if it is 0
void print_move(int move)
{
  if (move == -1){
    printf("O");
  } else if (move == 0){
    printf(" ");
  } else if (move == 1){
    printf("X");
  } else {
    printf("Error (print_move): Invalid move on the board, entry was %d\n", move);
  }
}


// print_board: prints the board in the terminal assuming 1 is X, -1 is O, 0 is blank
void print_board(int *board)
{
  for (int i = 0; i < 9; i++){
    printf(" ");
    print_move(board[i]);
    printf(" ");
    if ((i == 2) || (i == 5)){
      printf("\n-----------\n");
    } else if (i == 8){
      printf("\n\n");
    } else {
      printf("|");
    }
  }
}


// 


int main(){
  int board[] = {0, 0, 1, -1, -1, 1, 1, 0, 1};
//  int board1[] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
  print_board(board);
  return 0;
}
