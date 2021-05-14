#------------------------------------------------------------------------------ 
# For CS320 Principles of Programming Languages, Portland State University (JL)
#------------------------------------------------------------------------------ 
# RegEx Parser (top-down)
#
# Grammar: (c is a terminal representing a single letter)
#   e    -> alt
#   alt  -> seq {'|' seq}
#   seq  -> rep {rep}
#   rep  -> atom ['*']
#   atom -> '(' e ')' | c
#
# Usage: linux> ./python3 regex.py 'RE string'

# CS320 HW3 , Name : Shang Chun,Lin
import sys

def regex(str):
    i = 0  # idx to input string

    # lookahead the next char, return '$' if reaches the end
    def next():
        if i < len(str):
            return str[i]
        return '$'

    # match a char, advance the input idx
    def match(c):
        nonlocal i
        if str[i] == c:
            i += 1
        else:
            raise Exception("expected " + c + " got " + str[i])

    # alt -> seq {'|' seq}
    def alt():
        ast = seq()
        while next() == '|':
            match('|')
            ast = ['alt',ast,seq()]
        return ast
            
    # seq -> rep {rep}
    def seq():
        ast = ['seq']
        ast.append(rep())
        while next() == '(' or next().isalpha():
            if len(ast) >= 3:
                ast[2] = seq_recur(ast[2])
            else:
                ast.append(rep())
        
        if len(ast) < 3 and ast[0] == 'seq':
            ast.pop(0)
        return ast

    def seq_recur(inner_ast):
        if len(inner_ast) < 3:
            temp = ['seq']
            temp.append(inner_ast)
            temp.append(rep())
        else:
            temp = inner_ast[:2]
            smaller_list = inner_ast[2]
            temp.append(seq_recur(smaller_list))
        return temp

    # rep -> atom ['*']
    def rep():
        ast = ['rep']
        ast.append(atom())
        if next() == '*':
            match('*')
        else :
            ast.pop(0)
        return ast
    
    # atom -> '(' alt ')' | c
    def atom():
        if next() == '(':
            match('(')
            c = alt()
            match(')')
        else:
            c = next()
            if not c.isalpha():
                raise Exception("expected a letter, got " + c)
            match(c)
        return c

    def flatten(l):
        while len(l) == 1 and type(l[0]) == list:
            l = l.pop()
        return l

    # parsing starts here
    # e -> alt
    ast = alt()

    for k in range(len(ast)):
        ast[k] = flatten(ast[k])

    if i < len(str):
        raise Exception("found extra chars: " + str[i:])
    return ast

if __name__ == "__main__":
    ast = regex(sys.argv[1])
    print(ast)

