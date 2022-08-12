import numpy as np
from matplotlib import pyplot as plt

#fuzzy function== fuzzy fun curve equation

#general eqtion for incremnetal region =>
#var_val = (end_val-start_val)*fuzzy(sensor_val)+start_val

#general decrement
#var_val = -1*(end_val-start_val)*fuzzy(sensor_val)+end_val

#in steady state give end and start vales as same 


def vip_trapez_fuzzy(selector,start_val,end_val,emot_val):

    if selector==1:
        #shows incremental region
        val = (end_val-start_val)*emot_val+start_val

    elif selector==0:
        #steady state case
        start_val = end_val
        val = (end_val-start_val)*emot_val+start_val

    else:
        val=-1*(end_val-start_val)*emot_val+end_val

    return val


def sensor_motor_function(val):
    if val >0.9:
        
        return ag,fg,ar,fr,ab,fb

    elif val >0.8:
        #cb,ab,fb=section_one_F(val)
        ag,fg,ar,fr,ab,fb=section_four_A(val)
        return ag,fg,ar,fr,ab,fb

    elif val>0.5:
        ag,fg,ar,fr,ab,fb= section_three_A(val)
        return ag,fg,ar,fr,ab,fb
    
    elif val>0.4:
        ag,fg,ar,fr,ab,fb=section_two_A(val)
        return ag,fg,ar,fr,ab,fb
    
    elif val>0.3:
        ag,fg,ar,fr,ab,fb=section_three_L(val)
        #cr,ar,fr=section_one_A(val)
        return ag,fg,ar,fr,ab,fb

    else:
        ag,fg,ar,fr,ab,fb=section_zero(val)
        return ag,fg,ar,fr,ab,fb
        
