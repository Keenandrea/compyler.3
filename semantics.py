import collections
import sys
import token

var_count = 0
var_tally = 0
scope_init = 0
stack_max = 100
top_of_stack = 0
tos_offset = 0
stack = [99]

# for(int i = m; i >= lowest; i++)
# for i in range(m, low-1, -1)

# def build_stack():
#     token.Token.build_token_stack(stack)

def push(tk, var_count):
    #stack
    print "push with", tk.instance
    print "push var_count is", var_count
    if var_count >= stack_max:
        print "ERROR: Stack overflow"
        sys.exit(1)
    else:
        i = 0
        for i in xrange(scope_init, var_count, 1): 
            if stack[i].instance == tk.instance:
                print "ERROR:", tk.instance, "previously defined in this scope"
                sys.exit(1)
        stack[var_count] = tk
        var_count = var_count + 1


# def full_stack():
#     return top_of_stack ==  

# def empty_stack():
#     return top_of_stack == -1

def pop(scope_init, var_count): 
    print "pop"
    # remove top of stack
    i = 0
    for i in xrange(var_count, scope_init, -1):
        var_count = var_count - 1
        stack[i].instance == ""

def find(tk):
    print "\nfind with", tk.instance
    # find the first occurance
    # of the argument on the s
    # tack, starting from the
    # top and going down to th
    # bottom of the stack. ret
    # urn the distance from th
    # top of stack, where the 
    # item was found (0 if at
    # top of stack, or -1 if 
    # not found)
    for i in xrange(var_count, scope_init, -1):
        print scope_init, " ", var_count
        if stack[i].instance == tk.instance:
            tos_offset = var_count - 1 - i
            return tos_offset
    return -1

def var_in_scope(tk):
    print "var_in_scope"
    # look in stack for tk,
    # if tk is found in stack,
    # return true, otherwise r
    # eturn false
    i = 0
    for i in xrange(var_count - 1, -1, -1):
        if stack[i].instance == tk.instance:
            return True
    return False

"""
my var_tally is j's num_vars
my scope_init is j's scope_begin
my var_count is j's var_count
my tos_offset is j's tos_distance
"""

def verify_semantics(node, count):
    if node == None:
        return
    if node.label == "<program>":
        var_tally = 0
        if node.child1 != None:
            verify_semantics(node.child1, var_tally)
        if node.child2 != None:
            verify_semantics(node.child2, var_tally)
    elif node.label == "<vars>":
        tos_offset = find(node.token1)
        scope_init = var_count
        if tos_offset == -1 or tos_offset > count:
            push(node.token1, var_count)
            count = count + 1
        elif tos_offset < count:
            print "ERROR:", node.token1.instance, "previously defined in scope"
            sys.exit(1)
        if node.child1 != None:
            verify_semantics(node.child1, count)
    elif node.label == "<block>":
        var_tally = 0
        scope_init = var_count
        if node.child1 != None:
            verify_semantics(node.child1, var_tally)
        if node.child2 != None:
            verify_semantics(node.child2, var_tally)
        pop(scope_init, var_count)
    elif node.label == "<expr>":
        if node.token1.identity == "FSLASH_tk" or node.token1.identity == "ASTERISK_tk":
            if node.child1 != None:
                verify_semantics(node.child1, count)
            if node.child2 != None:
                verify_semantics(node.child2, count)
        elif node.child1 != None:
            verify_semantics(node.child1, count)
    elif node.label == "<A>":
        if node.token1.identity == "PLUS_tk" or node.token1.identity == "MINUS_tk":
            if node.child1 != None:
                verify_semantics(node.child1, count)
            if node.child2 != None:
                verify_semantics(node.child2, count)
        elif node.child1 != None:
            verify_semantics(node.child1, count)
    elif node.label == "<R>":
        if node.token1.identity == "ID_tk":
            if var_in_scope(node.token1) == False:
                print "ERROR:", node.token1.instance, "has not been declared in scope"
                sys.exit(1)
        elif node.child1 != None:
            verify_semantics(node.child1, count)
    elif node.label == "<in>":
        if var_in_scope(node.token1) == False:
            print "ERROR:", node.token1.instance, "has not been declared in scope"
            sys.exit(1)
    elif node.label == "<assign>":
        if var_in_scope(node.token1) == False:
            print "ERROR:", node.token1.instance, "has not been declared in scope"
            sys.exit(1)
        if node.child1 != None:
            verify_semantics(node.child1, count)
    else:
        if node.child1 != None:
            verify_semantics(node.child1, count)
        if node.child2 != None:
            verify_semantics(node.child2, count)
        if node.child3 != None:
            verify_semantics(node.child3, count)
        if node.child4 != None:
            verify_semantics(node.child4, count)


# FIND OUT WHY THE ABOVE CODE COMPLETES WITHOUT ERROR AND THE BELOW
# CODE FINDS AN INDEX ERROR WITH stack[i].instance == tk.instance

# import collections
# import sys
# import token

# class VCount:
#     def __init__(self, var_count, var_tally, scope_init, tos_offset):
#         self.var_count = var_count
#         self.var_tally = var_tally
#         self.scope_init = scope_init
#         self.tos_offset = tos_offset

# vc = VCount(0,0,0,0)

# stack_max = 100
# stack = [stack_max]

# # for(int i = m; i >= lowest; i++)
# # for i in range(m, low-1, -1)

# # def build_stack():
# #     token.Token.build_token_stack(stack)

# def push(tk):
#     #stack
#     print "push with", tk.instance
#     print "push var_count is", vc.var_count
#     if vc.var_count >= stack_max:
#         print "ERROR: Stack overflow"
#         sys.exit(1)
#     else:
#         i = 0
#         for i in xrange(vc.scope_init, vc.var_count, 1): 
#             if stack[i].instance == tk.instance:
#                 print "ERROR:", tk.instance, "previously defined in this scope"
#                 sys.exit(1)
#         stack[vc.var_count] = tk
#         vc.var_count = vc.var_count + 1


# # def full_stack():
# #     return top_of_stack ==  

# # def empty_stack():
# #     return top_of_stack == -1

# def pop(): 
#     print "pop"
#     # remove top of stack
#     i = 0
#     for i in xrange(vc.var_count, vc.scope_init, -1):
#         vc.var_count = vc.var_count - 1
#         stack[i].instance == ""

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
#     for i in xrange(vc.var_count, vc.scope_init, -1):
#         print vc.scope_init, " ", vc.var_count
#         if stack[i].instance == tk.instance:
#             vc.tos_offset = vc.var_count - 1 - i
#             return vc.tos_offset
#     return -1

# def var_in_scope(tk):
#     print "var_in_scope"
#     # look in stack for tk,
#     # if tk is found in stack,
#     # return true, otherwise r
#     # eturn false
#     i = 0
#     for i in xrange(vc.var_count - 1, -1, -1):
#         if stack[i].instance == tk.instance:
#             return True
#     return False

# """
# my vc.var_tally is j's num_vars
# my vc.scope_init is j's scope_begin
# my vc.var_count is j's vc.var_count
# my vc.tos_offset is j's tos_distance
# """

# def verify_semantics(node, count):
#     if node == None:
#         return
#     if node.label == "<program>":
#         vc.var_tally = 0
#         if node.child1 != None:
#             verify_semantics(node.child1, vc.var_tally)
#         if node.child2 != None:
#             verify_semantics(node.child2, vc.var_tally)
#     elif node.label == "<vars>":
#         vc.tos_offset = find(node.token1)
#         vc.scope_init = vc.var_count
#         if vc.tos_offset == -1 or vc.tos_offset > count:
#             push(node.token1)
#             count = count + 1
#         elif vc.tos_offset < count:
#             print "ERROR:", node.token1.instance, "previously defined in scope"
#             sys.exit(1)
#         if node.child1 != None:
#             verify_semantics(node.child1, count)
#     elif node.label == "<block>":
#         vc.var_tally = 0
#         vc.scope_init = vc.var_count
#         if node.child1 != None:
#             verify_semantics(node.child1, vc.var_tally)
#         if node.child2 != None:
#             verify_semantics(node.child2, vc.var_tally)
#         pop()
#     elif node.label == "<expr>":
#         if node.token1.identity == "FSLASH_tk" or node.token1.identity == "ASTERISK_tk":
#             if node.child1 != None:
#                 verify_semantics(node.child1, count)
#             if node.child2 != None:
#                 verify_semantics(node.child2, count)
#         elif node.child1 != None:
#             verify_semantics(node.child1, count)
#     elif node.label == "<A>":
#         if node.token1.identity == "PLUS_tk" or node.token1.identity == "MINUS_tk":
#             if node.child1 != None:
#                 verify_semantics(node.child1, count)
#             if node.child2 != None:
#                 verify_semantics(node.child2, count)
#         elif node.child1 != None:
#             verify_semantics(node.child1, count)
#     elif node.label == "<R>":
#         if node.token1.identity == "ID_tk":
#             if var_in_scope(node.token1) == False:
#                 print "ERROR:", node.token1.instance, "has not been declared in scope"
#                 sys.exit(1)
#         elif node.child1 != None:
#             verify_semantics(node.child1, count)
#     elif node.label == "<in>":
#         if var_in_scope(node.token1) == False:
#             print "ERROR:", node.token1.instance, "has not been declared in scope"
#             sys.exit(1)
#     elif node.label == "<assign>":
#         if var_in_scope(node.token1) == False:
#             print "ERROR:", node.token1.instance, "has not been declared in scope"
#             sys.exit(1)
#         if node.child1 != None:
#             verify_semantics(node.child1, count)
#     else:
#         if node.child1 != None:
#             verify_semantics(node.child1, count)
#         if node.child2 != None:
#             verify_semantics(node.child2, count)
#         if node.child3 != None:
#             verify_semantics(node.child3, count)
#         if node.child4 != None:
#             verify_semantics(node.child4, count)