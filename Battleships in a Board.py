class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        found = True
        while found:
            print "1"
            found = False
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == 'X':
                        count += 1
                        board[row][col] = '.'
                        found = True
                        i = 1
                        while col+i<len(board[row]) and board[row][col+i] == 'X':
                            board[row][col+i] = '.'
                            i+=1
                        i = 1
                        while row+i<len(board) and board[row+i][col] == 'X':
                            board[row+i][col] = '.'
                            i+=1
                    else:
                        continue     
        return count               