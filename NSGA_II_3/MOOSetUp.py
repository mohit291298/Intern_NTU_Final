##This is the script for setting up the multi-objective optimization 
def MOOSetUp ():
    
    import pandas as pd
    from nsga_2 import nsga_2

    allm_var = pd.DataFrame(columns = ['Name', 'Value', 'Unit', 'LB', 'UB', 'Type'])
    
    activate_parallel = 'no'
    num_cores = 4
    
    v1 = ['x1',10,'m',1,100,'continuous']
    v2 = ['x2',20,'m',1,100,'continuous']
    
    t11 = pd.DataFrame(data = [v1],columns = ['Name', 'Value', 'Unit', 'LB', 'UB', 'Type'])
    t12 = pd.DataFrame(data = [v2],columns = ['Name', 'Value', 'Unit', 'LB', 'UB', 'Type'])

    allm_var = allm_var.append(t11,ignore_index = True)
    allm_var = allm_var.append(t12,ignore_index = True)
    
    input_v = {}
    
    ##These are parameters for the genetic algorithm to work
    dim_allm_var = [2]
    
    input_v['population'] = 100
    input_v['generations'] = 50
    input_v['number_of_objectives'] = 2
    input_v['number_of_decision_variables'] = dim_allm_var[0]

    ##List of objective functions values 
    
    obj_v = pd.DataFrame(columns = ['Value'])
    
    ##1
    add_obj_v = {}
    add_obj_v['Value'] = 0
    
    input_add_obj_v = [add_obj_v['Value']]
    input_add_obj_vdf = pd.DataFrame(data = [input_add_obj_v], columns = ['Value'])
    obj_v = obj_v.append(input_add_obj_vdf, ignore_index=True)
    
    ##2
    add_obj_v = {}
    add_obj_v['Value'] = 0
    
    input_add_obj_v = [add_obj_v['Value']]
    input_add_obj_vdf = pd.DataFrame(data = [input_add_obj_v], columns = ['Value'])
    obj_v = obj_v.append(input_add_obj_vdf, ignore_index=True)
    
    input_v['obj_func_values'] = obj_v
    
    ##List of decision variables and their respective ranges 
    
    dv = pd.DataFrame(columns = ['Name', 'Initial_value', 'Unit', 'Min', 'Max', 'Type'])
    
    for i in range (0,dim_allm_var[0]):
        add_dv = {}
        add_dv['Name'] = allm_var['Name'][i]
        add_dv['Initial_value'] = allm_var['Value'][i]
        add_dv['Unit'] = allm_var['Unit'][i]
        add_dv['Min'] = allm_var['LB'][i]
        add_dv['Max'] = allm_var['UB'][i]
        add_dv['Type'] = allm_var['Type'][i]

        input_add_dv = [add_dv['Name'], add_dv['Initial_value'], add_dv['Unit'], add_dv['Min'], add_dv['Max'], add_dv['Type']]
        input_add_dvdf = pd.DataFrame(data = [input_add_dv], columns = ['Name', 'Initial_value', 'Unit', 'Min', 'Max', 'Type'])
        dv = dv.append(input_add_dvdf, ignore_index=True)
    
    input_v['range_of_decision_variables'] = dv
    
    ##Input the data into NSGA=II
    
    nsga_2(input_v,activate_parallel,num_cores)
    
    return
    
#####################################################################################################################################################
if __name__ == '__main__':
    import timing
    MOOSetUp ()