MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
    if maximizingPlayer:
        best = MIN
        #recur for left & right children
        for i in range(0, 2):
            val = minimax(depth+1, nodeIndex*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha,best)
            #alpha-beta pruning
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        #recur for left & right children
        for i in range(0, 2):
            val = minimax(depth+1, nodeIndex*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            #alpha-beta pruning
            if beta <= alpha:
                break
        return best

#driver code
if __name__ == '__main__':
    value = [3,5,7,9,1,2,0,-1]
    print("The optimal value is :", minimax(0,0,True,value,MIN,MAX))
            
                    
