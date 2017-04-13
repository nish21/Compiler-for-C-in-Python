import sys

import tokenize

symbolTable, inp_list = None, None
temp_count = 0
label_count = 0
i = 0
code = ""

def getNextToken():
    global i
    if i==len(inp_list):
        #print(i,-1)
        return -1
    i+=1
    return inp_list[i-1].id

def num(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def parse():
    global symbolTable, inp_list
    symbolTable, inp_list=tokenize.generateTokens()
    inp_list = inp_list[5:-4] #to ignore int main(){ return 0;}
    if(Statement()):
        print(code)
    else:
        print("Syntax error")

def Statements():
    if Statement():
        if Statements():
            return True
        else:
            return False
    elif i == len(inp_list)-1:
        return True
    else:
        return False

def Statement():
    global i, temp_count, label_count, code
    next=getNextToken()
    if next =="while":
        label_count += 1
        code += "L"+str(label_count)+":"
        next = getNextToken()
        if next == '(':
            if Cond():
                next = getNextToken()
                if next == ')':
                    code += "\nifFalse t" + str(temp_count)+ " goto L2"
                    next = getNextToken()
                    if next == '{':
                        if Statements():
                            next = getNextToken()
                            if next=='}':
                                code += "\ngoto L"+str(label_count)+"\n"
                                label_count += 1
                                code += "L"+str(label_count)+":\n"
                                return True
                            else:
                                print("Expected matching } in while")
                                sys.exit(1)
                        else:
                            sys.exit(1)
                            return False
                    else:
                        print("Expected { after ) in while")
                        sys.exit(1)
                        return False
                else:
                    print("Expected matching ) for while")
                    sys.exit(1)
                    return False
            else:
                sys.exit(1)
                return False
        else:
            print("Expected ( after while")
            return False
    #S-> ;S1
    elif next==";":
        new = getNextToken()
        i -= 1
        if Statements():
            return True
        else:
            print("Missing semicolon")
            return False
    elif Decl():
        next = getNextToken()
        if next==";":
            if Statements():
                return True
            else:
                print("Missing semic")
                return False

        return True
    elif Assign():
        return True
    else:
        return False

def Decl():
    global i
    i -= 1
    ret, inferred_type, size = Type()
    if ret:
        if Var(inferred_type, size):
            return True
        else:
            return False
    else:
        return False

def Type():
    global i
    next = getNextToken()
    if next=="int":
        return True, "int", 4
    elif next=="float":
        return True, "float", 4
    elif next=="char":
        return True, "char", 1
    elif next=="long":
        return True, "long", 8
    else:
        i -= 1
        return False, False, False
def Var(inferred_type, size):
    global symbolTable, i
    next = getNextToken()
    symbolTable.setDataType(next,inferred_type)
    symbolTable.setSize(next,size)
    if Var1(inferred_type, size):
        next = getNextToken()
        if next == ';':
            i-=1
            return True
        else:
            i-=1
            print("Missing semicolons")
            sys.exit(1)
            return False

def Var1(inferred_type, size):
    global i
    next = getNextToken()
    if next == ',':
        if Var(inferred_type, size):
            return True
        else:
            return False
    else:
        i -= 1
        return True

def Assign():
    global i, code
    next=getNextToken()
    temp = next
    if not num(next) and symbolTable.isVar(next):
        next=getNextToken()
        if next=="=":
            if E0():
                code += "\n"+temp + "= t"+str(temp_count)
                return True
            else:
                return False
        else:
            return False
    else:
        i-=1
        return False
    return False
'''
+--------------------------------------+
|                                      |
|           BRACE YOURSELVES.          |
|            WINTER IS HERE.           |
|                                      |
+--------------------------------------+
'''
def Cond():
    return E0()

def E0():
    global temp_count, code
    temp_count += 1
    code += "\nt"+str(temp_count)+" = "
    if E1():
        if E01():
            return True
        else:
            return False
    else:
        return False

def E01():
    global i, code
	#E01-> '||'E1E01 | e
    next=getNextToken()
    if next=="||":
        code += next
        if E1():
            if E01():
                return True
            else:
                return False
        else:
            return False
    else:
        i-=1
        return True

def E1():
    #E1-> E20E11
    if E20():
        if E11():
            return True
        else:
            return False
    else:
        return False

def E11():
    #E11-> &&E20E11 | e
    global i, code

    next=getNextToken()
    if next=="&&":
        code += next
        if E20():
            if E11():
                return True
            else:
                return False
        else:
            return False
    else:
        i-=1
        return True

def E20():
    #E20-> E2E201
    if E2():
        if E201():
            return True
        else:
            return False
    else:
        return False

def E201():
    #E201-> ==E2E201 | !=E2E201 | e
    global i, code

    next=getNextToken()
    if next=="==":
        code += next
        if E2():
            if E201():
                return True
            else:
                return False
        else:
            return False
    elif next=="!=":
        code += next
        if E2():
            if E201():
                return True
            else:
                return False
        else:
            return False

    else:
        i-=1
        return True

def E2():
	#E2-> E3E21
    if E3():
        if E21():
            return True
        else:
            return False
    else:
        return False

def E21():
    #E21-> >E22 | <E22 | e
    global i, code

    next=getNextToken()
    if next==">":
        code += next
        if E22():
            return True
        else:
            return False
    elif next=="<":
        code += next
        if E22():
            return True
        else:
            return False
    else:
        i-=1
        return True

def E22():
    #E22->  E3E21 | =E3E21
    if E3():
        if E21():
            return True
        else:
            return False
    else:
        next=getNextToken()
        if next=="=":
            code += next
            if E3():
                if E21():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

def E3():
	#E3-> E4E31
    if E4():
        if E31():
            return True
        else:
            return False
    else:
        return False

def E31():
	#E31-> +E4E31 | -E4E31 | e
    global i, code

    next=getNextToken()
    if next=="+":
        code += next
        if E4():
            if E31():
                return True
            else:
                return False
        else:
            return False
    elif next=="-":
        code += next
        if E4():
            if E31():
                return True
            else:
                return False
        else:
            return False
    else:
        i-=1
        return True

def E4():
	#E4-> E5E41
    if E5():
        if E41():
            return True
        else:
            return False
    else:
        return False

def E41():
	#E41-> *E5E41 | /E5E41 | e
    global i, code

    next=getNextToken()
    if next=="*":
        code += next
        if E5():
            if E41():
                return True
            else:
                return False
        else:
            return False
    elif next=="/":
        code += next
        if E5():
            if E41():
                return True
            else:
                return False
        else:
            return False
    else:
        i-=1
        return True

def E5():
	#E5->(E0) | id | num
    global i, symbolTable, code

    next=getNextToken()
    if next=="(":
        if E0():
            next=getNextToken()
            if next==")":
                return True
            else:
                print("Missing paranthesis")
                sys.exit(1)
                return False
        else:
            return False
    elif num(next):
        code += next
        return True

    elif not num(next):
        if symbolTable.isVar(next):
            code += next
            return True
        else:
            print("Unrecognized identifier "+next)
            sys.exit(1)
            return False
    else:
        return False
