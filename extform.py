#------------------------------------------------------------------------------ 
# For CS320 Principles of Programming Languages, Portland State University (JL)
#------------------------------------------------------------------------------ 
# Lab : convert an S-expression in string form to nested list form
# i.e. '(+ a (* b c))' => ['+', 'a', ['*', 'b', 'c']]
# (note: singletons stay the same: 'a' => 'a')

# Now we are going to do a reverse version!
# Write a Python function extform(lst) to
# convert an S-expression in list form into
# the string form.
# i.e.
#>>> s = ['+', 'a', ['*', 'b', 'c']]
#>>> extform(s)
#'(+ a (* b c))'

# CS320 HW3 , Name : Shang Chun,Lin
def extform(lst):
    x = str(tuple(lst))
    x = x.replace("'","").replace('[','(').replace(']',')').replace(',',' ')
    return x

if __name__ == "__main__":
    mylist = ['+', 'a', ['*', 'b', 'c']]
    print(extform(mylist))
