

def num_ways(amount, denominations):
    rows = len(denominations)
    columns = amount
    ##create a table of 0s specified number of rows and columns
    result_table = [[0 for c in range(columns+1)] for r in range(rows)]
    # print(result_table)

    ##add 1s to the 0th column. There is only one way to make a sum of 1
    for r in range(rows):
        result_table[r][0] = 1
    # print(result_table)

    #Use a recurrence relation to populate the table
    for i in range(rows):
        for j in range(1,columns+1):
            without_coin = (result_table[i-1][j] if i >= 1 else 0)
            with_coin = (result_table[i][j-denominations[i]] if j >= denominations[i] else 0)
            # print(i,j)
            result_table[i][j] =  (with_coin + without_coin)
    return result_table[-1][-1] ##return the last element in the table



# s = 4
# l = [1,2,3]

s = 3
l = [1,2,3]
# print(num_combinations_for_final_score(s,l))
print(num_ways(s,l))