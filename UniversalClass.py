###
### This class can be used as a template for 
### future UniversalClass creations, whose 
### methods can be used remotely (not in the same
### scope or function).
###

class UniversalClass:
    '''
    A template for a class whose functions
    can be accessed without an instance of that
    class.
    
    Beware of possible scope vulnerabilities.
    '''
    # Get instruction, gets all the available functions.
    @staticmethod
    def get():
        # Include all available methods here, as a scope.
        methods = ["get","load"]
        return [i for i in dir(UniversalClass) if i in methods]
    
    # Load instruction that loads, if possible, an available function from the main class.
    @staticmethod
    def load(instruction: str):
        try:
            global result
            exec(compile(f"result = UniversalClass.{instruction}","<string>","exec"), globals())
            local_var = globals().pop("result")
            return local_var
        
        except Exception:
            def Non():
                return None
            return Non