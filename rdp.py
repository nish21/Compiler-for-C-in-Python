def getNextToken():
    global i
    if i==len(inp_list):
        return -1
    i+=1
    return inp_list[i-1]

'''
S->while(C){S} | e | Ass | SS 

Ass-> id= E;
'''    
def S():
	global i
	next=getNextToken()
    
    #S->while(C){S} 
	if next=="while":
		j=i
        next=getNextToken()
        if next=="(":
            
            if C():
            	
            	next=getNextToken()
                if next==")":
                	
					next=getNextToken()
					if next=="{":
                    
						next=getNextToken()
						if S():
                        	
							next=getNextToken()
							if next=="}":return True
							'''
							else:i=j   
                                            
                                            
						else:i=j 
                			
					else:i=j 
                	
                else:i=j 
                                            
            else:i=j   
                    
		else:
			i=j  '''                                   
       
    #S-> e                            
	if next=="}":return True    
	                           
                                  
def C():
	next=getNextToken()
	next=getNextToken()
	next=getNextToken()
	return True
	#C-> E
	#return E()
    
'''    
def E():
	global i
	#E-> E||E1 | E1
    
    if E():
    	j=i
        next=getNextToken()
        
        
        if next=="||":
            if E():
                return True
            else:
                i=j
        else:
            i=j
        
    else:
        return E1()

        
def E1():
	
	E    
'''   
    	    
	        
        
        

'''
C-> E 
E-> E||E1 | E1
E1-> E1&&E2 | E2
E2-> E2>E3 | E2<E3 | E3
E3-> E3+E4 | E3-E4 | E4
E4-> E4*E5 | E4/E5 | E5
E5-> (E) | id | num



'''

   
i=0   

# while(2+3){}
inp_list=["while","(","2","+","3",")","{","}"]

print(S());
