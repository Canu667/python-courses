message = 'global'

def enclosing():
    message = 'enclosing'
    
    def local():
        global message
        message = 'local'
        
    def nonlocalF():
        nonlocal message
        message = 'nonlocal'    
        
    print('enclosing message:', message)
    local()
    nonlocalF()
    print('enclosing message:', message)
    
print('global message:', message)
enclosing()
print('global message:', message)