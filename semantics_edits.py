import collections
import sys

import node
import token
import semstack








# class Statics:
#     def __init__(self):
#         self.stack_size = 0
#         self.vars_count = 0
#         self.scope_init = 0
#         self.tos_offset = 0
# static = Statics()
# stack = semstack.SemStack()
# stack = [token.Token() for _ in range(100)]

# def push(tk):
#     print "push with", tk.instance
#     print "push stack_size is", static.stack_size
#     print "push scope_init is", static.scope_init
#     if static.stack_size >= 100:
#         print "ERROR: Stack overflow."
#         sys.exit(1)
#     else:
#         #i = 0
#         for i in xrange(static.scope_init, static.stack_size, 1): 
#             if stack[i].instance == tk.instance:
#                 print "ERROR:", tk.instance, "previously defined in this scope"
#                 sys.exit(1)
#         stack[static.stack_size] = tk
#         static.stack_size = static.stack_size + 1

# def pop(scope_init): 
#     print "pop"
#     # remove top of stack
#     #i = 0
#     for i in xrange(static.stack_size, scope_init, -1):
#         static.stack_size = static.stack_size - 1
#         stack[i].instance = ""
#         #stack[i].instance == ""

# def find(tk):
#     print "\nfind with", tk.instance
#     # find the first occurance
#     # of the argument on the s
#     # tack, starting from the
#     # top and going down to th
#     # bottom of the stack. ret
#     # urn the distance from th
#     # top of stack, where the 
#     # item was found (0 if at
#     # top of stack, or -1 if 
#     # not found)
#     #i = 0
#     for i in xrange(static.stack_size, static.scope_init - 1, -1):
#         print "iteration in find:", i
#         print "scope init:", static.scope_init, "var count:", static.stack_size
#         # if stack[i].instance == tk.instance and i == static.scope_init:
#         #     return 0
#         print "stack at:",stack[i].instance
#         print "tk.instance is:", tk.instance
#         if stack[i].instance == tk.instance:
#             static.tos_offset = static.stack_size - 1 - i
#             print "tos_offset in find:", static.tos_offset
#             return static.tos_offset
#     return -1

# def var_in_scope(tk):
#     print "var_in_scope"
#     # look in stack for tk,
#     # if tk is found in stack,
#     # return true, otherwise r
#     # eturn false
#     #i = 0
#     for i in xrange(static.stack_size - 1, -1, -1):
#         print "VAR IN SCOPE CHECKS STACK"
#         if stack[i].instance == tk.instance:
#             print "TRUE"
#             return True
#     return False

# """
# my static.vars_count is j's num_vars
# my static.scope_init is j's scope_begin
# my static.stack_size is j's static.stack_size
# my static.tos_offset is j's tos_distance
# """

# def static_semantics(node, count):
#     #print "count:", count
#     if node == None:
#         return
#     if node.label == "<program>":
#         static.vars_count = 0
#         if node.child1 != None:
#             static_semantics(node.child1, static.vars_count)
#         if node.child2 != None:
#             static_semantics(node.child2, static.vars_count)
#     elif node.label == "<vars>":
#         static.tos_offset = find(node.token1)
#         static.scope_init = static.stack_size
#         if static.tos_offset == -1 or static.tos_offset > count:
#             push(node.token1)
#             count = count + 1
#         elif static.tos_offset < count:
#             print "ERROR:", node.token1.instance, "previously defined in scope"
#             sys.exit(1)
#         if node.child1 != None:
#             static_semantics(node.child1, count)
#     elif node.label == "<block>":
#         static.vars_count = 0
#         static.scope_init = static.stack_size
#         if node.child1 != None:
#             static_semantics(node.child1, static.vars_count)
#         if node.child2 != None:
#             static_semantics(node.child2, static.vars_count)
#         pop(static.scope_init)
#     elif node.label == "<expr>":
#         if node.token1.identity == "FSLASH_tk" or node.token1.identity == "ASTERISK_tk":
#             if node.child1 != None:
#                 static_semantics(node.child1, count)
#             if node.child2 != None:
#                 static_semantics(node.child2, count)
#         elif node.child1 != None:
#             static_semantics(node.child1, count)
#     elif node.label == "<A>":
#         if node.token1.identity == "PLUS_tk" or node.token1.identity == "MINUS_tk":
#             if node.child1 != None:
#                 static_semantics(node.child1, count)
#             if node.child2 != None:
#                 static_semantics(node.child2, count)
#         elif node.child1 != None:
#             static_semantics(node.child1, count)
#     elif node.label == "<R>":
#         if node.token1.identity == "ID_tk":
#             if var_in_scope(node.token1) == False:
#                 print "ERROR:", node.token1.instance, "has not been declared in scope"
#                 sys.exit(1)
#         elif node.child1 != None:
#             static_semantics(node.child1, count)
#     elif node.label == "<in>":
#         if var_in_scope(node.token1) == False:
#             print "ERROR:", node.token1.instance, "has not been declared in scope"
#             sys.exit(1)
#     elif node.label == "<assign>":
#         if var_in_scope(node.token1) == False:
#             print "ERROR:", node.token1.instance, "has not been declared in scope"
#             sys.exit(1)
#         if node.child1 != None:
#             static_semantics(node.child1, count)
#     else:
#         if node.child1 != None:
#             static_semantics(node.child1, count)
#         if node.child2 != None:
#             static_semantics(node.child2, count)
#         if node.child3 != None:
#             static_semantics(node.child3, count)
#         if node.child4 != None:
#             static_semantics(node.child4, count)


# class Statics:
#     def __init__(self):
#         self.stack_size = 0
#         self.vars_count = 0
#         self.scope_init = 0
#         self.tos_offset = 0
# static = Statics()

# # class Stack:
# #     def __init__(self):
# #         self.size = 0
# #         self.  
# LIMIT = 100
# stack = [token.Token() for _ in range(LIMIT)]

# # for(int i = m; i >= lowest; i++)
# # for i in range(m, low-1, -1)

# def push(tk):
#     print "push with", tk.instance
#     print "push stack_size is", static.stack_size
#     print "push scope_init is", static.scope_init
#     if static.stack_size >= LIMIT:
#         print "ERROR: Stack overflow"
#         sys.exit(1)
#     else:
#         #i = 0
#         for i in xrange(static.scope_init, static.stack_size, 1): 
#             if stack[i].instance == tk.instance:
#                 print "ERROR:", tk.instance, "previously defined in this scope"
#                 sys.exit(1)
#         stack[static.stack_size] = tk
#         static.stack_size = static.stack_size + 1

# def pop(scope_init): 
#     print "pop"
#     # remove top of stack
#     #i = 0
#     for i in xrange(static.stack_size, scope_init, -1):
#         static.stack_size = static.stack_size - 1
#         stack[i].instance = ""
#         #stack[i].instance == ""

# def find(tk):
#     print "\nfind with", tk.instance
#     # find the first occurance
#     # of the argument on the s
#     # tack, starting from the
#     # top and going down to th
#     # bottom of the stack. ret
#     # urn the distance from th
#     # top of stack, where the 
#     # item was found (0 if at
#     # top of stack, or -1 if 
#     # not found)
#     #i = 0
#     for i in xrange(static.stack_size, static.scope_init - 1, -1):
#         print "iteration in find:", i
#         print "scope init:", static.scope_init, "var count:", static.stack_size
#         # if stack[i].instance == tk.instance and i == static.scope_init:
#         #     return 0
#         print "stack at:",stack[i].instance
#         print "tk.instance is:", tk.instance
#         if stack[i].instance == tk.instance:
#             static.tos_offset = static.stack_size - 1 - i
#             print "tos_offset in find:", static.tos_offset
#             return static.tos_offset
#     return -1

# def var_in_scope(tk):
#     print "var_in_scope"
#     # look in stack for tk,
#     # if tk is found in stack,
#     # return true, otherwise r
#     # eturn false
#     #i = 0
#     for i in xrange(static.stack_size - 1, -1, -1):
#         print "VAR IN SCOPE CHECKS STACK"
#         if stack[i].instance == tk.instance:
#             print "TRUE"
#             return True
#     return False

# """
# my static.vars_count is j's num_vars
# my static.scope_init is j's scope_begin
# my static.stack_size is j's static.stack_size
# my static.tos_offset is j's tos_distance
# """

# def static_semantics(node, count):
#     #print "count:", count
#     if node == None:
#         return
#     if node.label == "<program>":
#         static.vars_count = 0
#         if node.child1 != None:
#             static_semantics(node.child1, static.vars_count)
#         if node.child2 != None:
#             static_semantics(node.child2, static.vars_count)
#     elif node.label == "<vars>":
#         static.tos_offset = find(node.token1)
#         static.scope_init = static.stack_size
#         if static.tos_offset == -1 or static.tos_offset > count:
#             push(node.token1)
#             count = count + 1
#         elif static.tos_offset < count:
#             print "ERROR:", node.token1.instance, "previously defined in scope"
#             sys.exit(1)
#         if node.child1 != None:
#             static_semantics(node.child1, count)
#     elif node.label == "<block>":
#         static.vars_count = 0
#         static.scope_init = static.stack_size
#         if node.child1 != None:
#             static_semantics(node.child1, static.vars_count)
#         if node.child2 != None:
#             static_semantics(node.child2, static.vars_count)
#         pop(static.scope_init)
#     elif node.label == "<expr>":
#         if node.token1.identity == "FSLASH_tk" or node.token1.identity == "ASTERISK_tk":
#             if node.child1 != None:
#                 static_semantics(node.child1, count)
#             if node.child2 != None:
#                 static_semantics(node.child2, count)
#         elif node.child1 != None:
#             static_semantics(node.child1, count)
#     elif node.label == "<A>":
#         if node.token1.identity == "PLUS_tk" or node.token1.identity == "MINUS_tk":
#             if node.child1 != None:
#                 static_semantics(node.child1, count)
#             if node.child2 != None:
#                 static_semantics(node.child2, count)
#         elif node.child1 != None:
#             static_semantics(node.child1, count)
#     elif node.label == "<R>":
#         if node.token1.identity == "ID_tk":
#             if var_in_scope(node.token1) == False:
#                 print "ERROR:", node.token1.instance, "has not been declared in scope"
#                 sys.exit(1)
#         elif node.child1 != None:
#             static_semantics(node.child1, count)
#     elif node.label == "<in>":
#         if var_in_scope(node.token1) == False:
#             print "ERROR:", node.token1.instance, "has not been declared in scope"
#             sys.exit(1)
#     elif node.label == "<assign>":
#         if var_in_scope(node.token1) == False:
#             print "ERROR:", node.token1.instance, "has not been declared in scope"
#             sys.exit(1)
#         if node.child1 != None:
#             static_semantics(node.child1, count)
#     else:
#         if node.child1 != None:
#             static_semantics(node.child1, count)
#         if node.child2 != None:
#             static_semantics(node.child2, count)
#         if node.child3 != None:
#             static_semantics(node.child3, count)
#         if node.child4 != None:
#             static_semantics(node.child4, count)






class Counters:
    def __init__(self):
        self.stack_size = 0
        self.vars_count = 0
        self.scope_init = 0
        self.tos_offset = 0
c = Counters()



class S:
    def __init__(self, vars_count = 0):
        #self.stack_size = 0
        self.vars_count = vars_count
        #self.scope_init = 0
        #self.tos_offset = 0
        #self.tkns = []

s = S()
stack = semstack.SemStack()


# for(int i = m; i >= lowest; i++)
# for i in range(m, low-1, -1)

def build_stack(measure):
    if measure > 100:
        print "ERROR: Stack overflow."
        sys.exit(1)
    stack.sem_stack = [token.Token() for _ in xrange(measure)]
    stack.size = measure
    stack.top = -1

def is_full():
    if stack.top == stack.size - 1:
      return True
    else:
      return False

def is_empty():
    if stack.top == -1:
      return True
    else:
      return False

def verify(tk):
    print "landed in verify with", tk
    in_stack = False
    if is_empty() == True:
        return False
    else:
        # i--
        for i in xrange(stack.top,-1,-1):
            if stack.sem_stack[i].instance == tk:
                in_stack = True
                break
        return in_stack

def find(tk):
    position = -1
    i = 0 
    j = stack.top 
    print "looking for stack value:", stack.sem_stack[j - i], "at position", (j-i), "to match against token value:", tk
    while i <= j:
        if stack.sem_stack[j - i] == tk: 
            position = i
            print "found", stack.sem_stack[j - i], "at stack position", i
            break
        # i++
        i += 1
    if position == -1:
        print tk, "not found in stack"
    print "return position as", position, "in find"
    return position

def pop():
    if is_empty() == False:
        # i--
        stack.top -= 1
        print "popping stack. top is now:", stack.top

def push(tk):
    print "\ngot to push func"
    if is_full() == False:
        stack.top += 1
        stack.sem_stack[stack.top] = tk
        print "\npushing token", tk, "onto stack position", stack.top, "which is the top"

def stack_position(node):
    print "made it to stack_pos"
    position = -1
    # ++i
    for i in xrange(0,len(node.toks),1):
        instance = node.toks[i].instance
        position = find(instance)
        if position == -1:
            print "in stack_pos"
            if verify(instance) == False:
                print "ERROR:", instance, "is undefined"
                sys.exit(1)
        return position
    return position

def push_instance(node):
    # ++i
    for tkn in node.toks:
        instance = tkn.instance
        if s.vars_count > 0:
            print "\ncounted", s.vars_count, "vars"
            position = find(instance)
            print "position in push_instance is", position
            if position >= 0 and position < s.vars_count:
                # THIS IS MALFUNCTIONING
                print "ERROR:", instance, "previously defined in scope"
                sys.exit(1)
        push(instance)
        # i++
        s.vars_count += 1

def static_semantics(node,counter):
    # if node != None:
    #     for tkn in node.toks:
    #         if tkn.instance[0].islower() == True: 
    #             print "toks:", tkn.instance
    #     print "\n"

    if node == None:
        return

    if node.label == "<program>":
        static_semantics(node.child1,)
        static_semantics(node.child2,)


    elif node.label == "<vars>":
        push_instance(node)
        static_semantics(node.child1)


    elif node.label == "<block>":
        temps_count = s.vars_count
        s.vars_count = 0
        static_semantics(node.child1)
        static_semantics(node.child2)
        for i in xrange(0,s.vars_count,1):
            pop()
        s.vars_count = temps_count


    elif node.label == "<expr>":
        if node.child2 == None:
            static_semantics(node.child1)
        else:
            static_semantics(node.child2)
            static_semantics(node.child1)


    elif node.label == "<A>":
        if node.child2 == None:
            static_semantics(node.child1)
        else:
            static_semantics(node.child2)
            static_semantics(node.child1)

    
    elif node.label == "<M>":
        if (node.child1).label == "<M>":
            static_semantics(node.child1)
        else:
            static_semantics(node.child1)


    elif node.label == "<N>":
        if node.child2 == None:
            static_semantics(node.child1)
        else:
            static_semantics(node.child2)
            static_semantics(node.child1)


    elif node.label == "<R>":
        if node.child1 != None:
            static_semantics(node.child1)
        else:
            if (node.toks)[0].identity == "INT_tk":
                print (node.toks)[0].identity 
            else:
                print "R calls to stack_pos"
                position = stack_position(node)


    elif node.label == "<in>":
        position = stack_position(node)
    

    elif node.label == "<out>":
        static_semantics(node.child1)

    
    # STILL NEED IF AND LOOP AND RO IN THEM


    elif node.label == "<assign>":
        static_semantics(node.child1)
        position = stack_position(node)


    else:
        static_semantics(node.child1)
        static_semantics(node.child2)
        static_semantics(node.child3)
        static_semantics(node.child4)