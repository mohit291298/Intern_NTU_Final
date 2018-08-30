##This function performs the mutation of the newly generated pool 

def ga_mono_mutation (parent_pool,mutation_prob):
    
    import numpy as np
    import math
    
    ##parent_pool --- the pool of original selected parents
    ##child_pool --- the offsprings of the parents 
    ##mutation_perc --- the percentage of the total bits which will be switched
    ##mutation_prob --- the probability of bits mutation
    
    ##Combining the parent and child pools 
    combined_pool = parent_pool
    
    ##Determining the total number of bits
    dim_combined_pool = combined_pool.shape 
    bit_len = dim_combined_pool[1] - 3                  ##The last 2 columns are for the objective function and the fitness respectively 
    mutation_perc = uniform(0,1)
    if mutation_perc <0.5 :
        mutation_perc = 0.5
    bits_to_mutate = math.ceil(mutation_perc * bit_len)
    
    ##Making a copy of the combined_pool
    combined_pool_copy = np.copy(combined_pool)
    row = np.random.choice(range(dim_combined_pool[0]))
    columns = np.random.choice(range(dim_combined_pool[1] - 3), bits_to_mutate, p = mutation_prob)

    for i in range (0, bits_to_mutate):

       #column = np.random.choice(range(dim_combined_pool[1] - 3), p = mutation_prob)
       if int(combined_pool_copy[row, columns[i]]) == 0:
           combined_pool_copy[row, columns[i]] = 1
       else:
           combined_pool_copy[row, columns[i]] = 0

    return combined_pool_copy