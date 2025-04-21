def main():
    n = int(input("Enter the number of Queen : "))
    board = [[0 for _ in range(n)]for _ in range(n)]
    solution = []

    nqueen(board,0,n,solution)
    print(solution)


def nqueen(board,col,n,solution):
    if col==n:
        solution.append([row[:] for row in board])
        return
    
    for i in range(n):
        if issafe(board,i,col,n):
            board[i][col] = 1
            nqueen(board,col+1,n,solution)
            board[i][col] = 0






def issafe(board,row,col,n):
    for i in range (col):
        if board[row][i] == 1 :
            return False

    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    for i,j in zip(range(row,n),range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    return True    

   


if __name__ == "__main__":
    main()
    