def main():
    n = int(input("Enter the number Queens : "))
    grid = [[0 for _ in range (n)] for _ in range (n)]
    Solution = []
    nQueen(grid,Solution,0,n)
    j = 1
    for i in Solution:
        print(f"Solution {j}")
        j = j +1
        for k in i:
            print(k)




def nQueen(grid,solutions,col,n):
    if col == n:
        solutions.append([row[:] for row in grid])  
        return
    
    for i  in range(n):
        if issafe(grid,i,col,n):
          grid[i][col]=1
          nQueen(grid,solutions,col+1,n)
          grid[i][col]=0


def issafe(grid,row,col,n):
    for i in range (col):
        if grid[row][i] == 1:
            return False
        
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if grid[i][j]==1:
            return False

    for i,j in zip(range(row,n),range(col,-1,-1)):
        if grid[i][j]==1:
            return False

    return True       


if __name__ == "__main__":
    main()
