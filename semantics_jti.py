import collections
import sys

import node
import token
import semstack

class Counters:
    def __init__(self):
        #self.scope_close = 0
        self.vcount = 0
        self.tcount = 0
        #self.scope_init = 0
        #self.tos_offset = 0

c = Counters()
s = semstack.SemStack()

def build_stack(length):
    if length > 100:
        print "ERROR: Stack overflow."
        sys.exit(1)
    else:
        s.scope_start = 0
        # s.scope = [token.Token()]
        s.scope = [token.Token() for _ in xrange(length)]
        for i in xrange(0,len(s.scope),1):
            s.scope[i].instance = ""

def is_full():
    if s.scope_start >= len(s.scope) - 1:
      return True
    else:
      return False

def is_empty():
    if s.scope_start == 0:
      return True
    else:
      return False

def scope_find(tk):
    print "\ngot to find"
    i = c.vcount
    j = s.scope_start
    print "find iters c.vcount:", i, "s.scope_start:", j
    while i >= j:
        if s.scope[i].instance == tk.instance:
            return c.vcount - 1 - i
        i -= 1
    return -1

def scope_pop(scope_start):
    print "got to pop"
    if is_empty() == False:
        i = c.vcount
        j = scope_start
        while i > j:
            c.vcount -= 1
            s.scope[i].instance == ""
            # s.scope[i].instance = ""
            i -= 1

def scope_push(tk):
    for v in s.scope:
        if v.instance is not "":
            print v.instance
    if is_full() == False:
        i = s.scope_start
        j = c.vcount
        print "\npush iters s.scope_start:", i, "c.vcount:", j
        while i < j:
            if s.scope[i].instance == tk.instance:
                print "ERROR:", tk.instance, "previously defined within scope"
                sys.exit(1)
            i += 1
        print "pushing", tk.instance, "onto s.scope at", c.vcount
        s.scope[c.vcount] = tk
        c.vcount += 1

def var_in_scope(tk):
    i = c.vcount - 1
    while i > -1:
        if s.scope[i].instance == tk.instance:
            print tk.instance, "found at", c.vcount - 1 - i
            return c.vcount - 1 - i
        else:
            print tk.instance, "isn't at", c.vcount - 1 - i
        i -= 1
    return -1

def static_semantics(node,counter):
    if node == None:
        return
    else:
        node_label = node.label

        if node_label == "<program>":
            program_variables = 0
            if node.child1 != None:
                static_semantics(node.child1,program_variables)
            if node.child2 != None:
                static_semantics(node.child2,program_variables)

        elif node_label == "<vars>":
            offset = scope_find(node.token1)
            s.scope_start = c.vcount
            if offset == -1 or offset > counter:
                scope_push(node.token1)
                counter += 1
            elif offset < counter:
                print "ERROR:", node.token1.instance, "previously defined within scope"
                sys.exit(1)
            if node.child1 != None:
                static_semantics(node.child1,counter)

        elif node_label == "<block>":
            block_variables = 0
            s.scope_start = c.vcount
            print "in <block> s.scope_start is", s.scope_start, "c.vcount is", c.vcount
            if node.child1 != None:
                static_semantics(node.child1,block_variables)
            if node.child2 != None:
                static_semantics(node.child2,block_variables)
            print "in <block> passing to scope_pop s.scope_start is", s.scope_start
            scope_pop(s.scope_start)

        elif node_label == "<expr>":
            if node.token1.identity == "PLUS_tk":
                if node.child2 != None:
                    static_semantics(node.child2,counter)
                if node.child1 != None:
                    static_semantics(node.child1,counter)
            elif node.child1 != None:
                static_semantics(node.child1,counter)

        elif node_label == "<A>":
            if node.token1.identity == "MINUS_tk":
                if node.child2 != None:
                    static_semantics(node.child2,counter)
                if node.child1 != None:
                    static_semantics(node.child1,counter)
            elif node.child1 != None:
                static_semantics(node.child1,counter)
     
        elif node_label == "<M>":
            if node.token1.identity == "MINUS_tk":
                if node.child1 != None:
                    static_semantics(node.child1, counter)
            else:
                if node.child1 != None:
                    static_semantics(node.child1,counter)

        elif node_label == "<N>":
            if node.token1.identity == "FSLASH_tk":
                if node.child2 != None:
                    static_semantics(node.child2,counter)
                if node.child1 == None:
                    static_semantics(node.child1,counter)
            elif node.token1.identity == "ASTERISK_tk":
                if node.child2 != None:
                    static_semantics(node.child2,counter)
                if node.child1 != None:
                    static_semantics(node.child1,counter)
            elif node.child1 != None:
                static_semantics(node.child1,counter)

        elif node_label == "<R>":
            if node.token1.identity == "ID_tk":
                var_pos = var_in_scope(node.token1)
                if var_pos == -1:
                    print "ERROR", node.token1.instance, "undeclared within scope"
                    sys.exit(1)
            elif node.token1.identity == "INT_tk":
                print "LOAD", node.token1.instance
            elif node.child1 != None:
                static_semantics(node.child1,counter)

        elif node_label == "<in>":
            var_pos = var_in_scope(node.token1)
            if var_pos == -1:
                print "ERROR", node.token1.instance, "undeclared within scope"
                sys.exit(1)   
        
        elif node_label == "<out>":
            if node.child1 != None:
                static_semantics(node.child1,counter)
        
        # STILL NEED IF AND LOOP AND RO IN THEM

        elif node_label == "<assign>":
            if node.child1 != None:
                static_semantics(node.child1,counter)
            var_pos = var_in_scope(node.token1)
            if var_pos == -1:
                print "ERROR", node.token1.instance, "undeclared within scope"
                sys.exit(1)

        else:
            if node.child1 != None:
                static_semantics(node.child1,counter)
            if node.child2 != None:
                static_semantics(node.child2,counter)
            if node.child3 != None:
                static_semantics(node.child3,counter)
            if node.child4 != None:
                static_semantics(node.child4,counter)