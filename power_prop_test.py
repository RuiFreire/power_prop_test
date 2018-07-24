from scipy.stats import norm
from sympy.solvers import solve
from sympy import Symbol

def calc_z_quantiles(p1, p2, alpha, power):
    
    if power == None:

        if p2 > p1:
            Zalpha = norm.ppf(1 - alpha)
        else:
            Zalpha = norm.ppf(alpha)
        
        return Zalpha    
    
    elif alpha == None:
        
        
        if p2 > p1:
            Zbeta = norm.ppf(1 - power)
        else:
            Zbeta = norm.ppf(power)
        
        return Zbeta    
      
    else:
        
        if p2 > p1:
            Zalpha = norm.ppf(1 - alpha)
            Zbeta = norm.ppf(power)
        else:
            Zalpha = norm.ppf(alpha)
            Zbeta = norm.ppf(1-power)

        return Zalpha, Zbeta
        

def get_values(first_value, second_value):
    
    values_list = []
    
    try:
        first_value = first_value.args[0]
    except:
        pass
    
    if first_value >= 0 and first_value <= 1:
        values_list.append(first_value)
    
    try:
        second_value = second_value.args[0] 
    except:
        pass
    
    if second_value >= 0 and second_value <= 1:
        values_list.append(second_value)
    
    return values_list

    
def power_prop_test(p1=None, p2=None, n=None, sig_level=0.05, power=None, alternative = "two.sided"):
    
    args_list = [p1, p2, n, sig_level, power, alternative]
    
    sum_of_nones = 0
    
    for arg in args_list:
        if arg == None:
            sum_of_nones += 1
            
    if sum_of_nones != 1:
        print("Exactly one of 'n', 'p1', 'p2', 'power', and 'alpha' must be NULL")
        return None
        
    if alternative == "two.sided" and sig_level != None:
        alpha = sig_level/2
    else:
        alpha = sig_level
    
    if p1 == None:
        
        Zalpha = norm.ppf(1 - alpha)
        Zbeta = norm.ppf(power)
        
        x = Symbol('x')
        
        p1_first_value = solve( x-p2 + Zalpha*( ((x + p2) / 2)*( 1 - ((x + p2) / 2) )*(2/n) )**(1/2) + Zbeta*( (x*(1-x) + p2*(1-p2))/n )**(1/2), x)[0]   
        print(p1_first_value)        
            
        Zalpha = norm.ppf(alpha)
        Zbeta = norm.ppf(1-power)
        
        x = Symbol('x')
        
        p1_second_value = solve( x-p2 + Zalpha*( ((x + p2) / 2)*( 1 - ((x + p2) / 2) )*(2/n) )**(1/2) + Zbeta*( (x*(1-x) + p2*(1-p2))/n )**(1/2), x)[0]   
        print(p1_second_value)
        
        p1_values = get_values(p1_first_value, p1_second_value)
        
        if len(p1_values) == 2:
            print("p1 = {} or p1 = {}".format(p1_values[0], p1_values[1]) )
        else:
            print("p1 = {}".format(p1_values[0]) )
        
    if p2 == None:
            
        Zalpha = norm.ppf(1 - alpha)
        Zbeta = norm.ppf(power)
        
        x = Symbol('x')
        
        p2_first_value = solve( p1-x + Zalpha*( ((p1 + x) / 2)*( 1 - ((p1 + x) / 2) )*(2/n) )**(1/2) + Zbeta*( (p1*(1-p1) + x*(1-x))/n )**(1/2), x)[0]    
                
        Zalpha = norm.ppf(alpha)
        Zbeta = norm.ppf(1-power)
        
        x = Symbol('x')
        
        p2_second_values = solve( p1-x + Zalpha*( ((p1 + x) / 2)*( 1 - ((p1 + x) / 2) )*(2/n) )**(1/2) + Zbeta*( (p1*(1-p1) + x*(1-x))/n )**(1/2), x)[0]    
    
        p2_values = get_values(p2_first_value, p2_second_value)
        
        if len(p2_values) == 2:
            print("p2 = {} or p2 = {}".format(p1_values[0], p1_values[1]) )
        else:
            print("p2 = {}".format(p1_values[0]) )
           
         
    if n == None:
        
        Zalpha, Zbeta = calc_z_quantiles(p1, p2, alpha, power)
        
        po = (p1 + p2) / 2

        x = Symbol('x')

        n = solve( p1-p2 + Zalpha*(po*(1-po)*(2/x))**(1/2) + Zbeta*( (p1*(1-p1) + p2*(1-p2))/x )**(1/2), x )[0]
          
            
    if power == None:
                            
        po = (p1 + p2) / 2            
        
        Zalpha = calc_z_quantiles(p1, p2, alpha, power)
        
        Zc = p1 + Zalpha*np.sqrt( po*(1-po)*(2/n) )

        if p2 > p1:
            power = norm.sf(Zc, loc=p2, scale = np.sqrt( (p1*(1 - p1) + p2*(1-p2))/n) )
        else:
            power = norm.cdf(Zc, loc=p2, scale = np.sqrt( (p1*(1 - p1) + p2*(1-p2))/n) )
        
        
    if alpha == None:
                    
        po = (p1 + p2) / 2                        
        
        Zbeta = calc_z_quantiles(p1, p2, alpha, power)
        
        Zc = p2 + Zbeta*np.sqrt( (p1*(1 - p1) + p2*(1-p2))/n )

        if p2 > p1:
            alpha = norm.sf(Zc, loc=p1, scale = np.sqrt( po*(1-po)*(2/n) ) )
        else:
            alpha = norm.cdf(Zc, loc=p1, scale = np.sqrt( po*(1-po)*(2/n) ) )
            
        if alternative == "two.sided":
            sig_level = 2*alpha
        else:
            sig_level = alpha
    
    if p1 != None:
        print("p1 = {}".format(p1))

    if p2 != None:
        print("p2 = {}".format(p2))

    print("n = {}".format(n))
    print("sig_level = {}".format(sig_level))
    print("power = {}".format(power))
    print("alternative = "+ alternative)
                 
