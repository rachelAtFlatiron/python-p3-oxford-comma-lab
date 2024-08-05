import ipdb 

one = ['a']
two = ['a', 'b']
test = ['a', 'b', 'c', 'd', 'e', 'f']

#takes in a list
def oxford_comma(items):
    #Case 1: 1 element
    if(len(items) == 1):
        return items[0]
    #Case 2: 2 elements
    elif(len(items) == 2):
        return f'{items[0]} and {items[1]}'
    #Case 3:
    else:
        #creates a new string where
        #each item is separated by a comma EXCEPT
        #the last item will be separate by a comma and the word 'and'
        ret_str = ', '.join(items[:len(items) - 1]) #'a, b, c, d, e, f'
        #'a, b, c, d, e, and f'
        ret_str = ret_str + f', and {items[len(items) - 1]}'
        return ret_str
