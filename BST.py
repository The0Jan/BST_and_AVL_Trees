
class Branch:
    def __init__(self, value):
        self.value = value
        self.leftStick = None
        self.rightStick = None
        self.times = 1 
        self.elderStick = None


class Tree:
    def __init__(self):
        self.root = None

    def creator(self,listed =[]):
        for i in listed:
            self.insert(i)

    def destructor(self, listed=[]):
        for i in listed:
            self.get_rid(i)

    #a simple function that leads to a recursive fucntion
    def insert(self, number):
        if self.root==None:
            self.root = Branch(number)
        else: 
            self.deep_insert(number, self.root)

    #Depending on the value, lead a way through the barnches untill met with the the existing value, or at the end
    def deep_insert(self,number,now_branch ):
            if number < now_branch.value:
                if now_branch.leftStick == None:
                    now_branch.leftStick = Branch(number)
                    now_branch.leftStick.elderStick = now_branch
                else:
                    self.deep_insert(number, now_branch.leftStick, )
            elif number > now_branch.value:
                if now_branch.rightStick == None:
                    now_branch.rightStick = Branch(number)
                    now_branch.rightStick.elderStick = now_branch

                else:
                    self.deep_insert(number, now_branch.rightStick)
            else:
                now_branch.times = now_branch.times + 1
              #  print("The number:" + str(number) + " occured " + str(now_branch.times))

    def print(self):
         if self.root != None:
            self.rec_print(self.root)

    def rec_print(self, now_branch):
        if now_branch != None:
            self.rec_print(now_branch.leftStick)
            print(str(now_branch.value))
            self.rec_print(now_branch.rightStick)
        
    def find_branch(self, value):
        if self.root != None:
            return self.find_value(value, self.root)
        else:
            return None
    #Recursive function for going down and searching the tree
    def find_value(self, value, now_branch):
        if value == now_branch.value:
            return now_branch
        elif value < now_branch.value and now_branch.leftStick != None:
            return self.find_value(value, now_branch.leftStick)
        elif value > now_branch.value and now_branch.rightStick !=None:
            return self.find_value(value, now_branch.rightStick)

    def get_rid(self, value):
        return self.get_rid_rec(self.find_branch(value))

    #recursive function that delets a branch: follows three cases
    def get_rid_rec(self, branch):
        if branch ==None or self.find_branch(branch.value) == None:
            return None

        if branch.times > 1:
        #    print("remaining:" + str(branch.times))
            branch.times = branch.times -1
        else:
            
            def how_many_sticks(branch):
                num_sticks = 0
                if branch.leftStick != None:
                    num_sticks = num_sticks + 1
                if branch.rightStick != None:
                    num_sticks = num_sticks + 1
                return num_sticks

            # case 1: The branch we are at has no stick, there are no branches down
            if how_many_sticks(branch) == 0:
                if branch.elderStick != None:
                    if branch.elderStick.leftStick == branch:
                        branch.elderStick.leftStick = None
                    else:
                        branch.elderStick.rightStick = None
                else:
                    self.root = None

            # case 2: The branch has one stick: replace the branch we are at with the stick(in case of root, the stick replaces the root)
            if how_many_sticks(branch) == 1: 
                
                if branch.leftStick != None:
                    small_stick = branch.leftStick
                else: 
                    small_stick = branch.rightStick

                if branch.elderStick != None:
                    if branch.elderStick.leftStick == branch:
                        branch.elderStick.leftStick = small_stick
                    else:
                        branch.elderStick.rightStick = small_stick
                else:
                    self.root = small_stick

                small_stick.elderStick = branch.elderStick

            def give_smallest_stick(given_value):
                current_value = given_value
                if current_value.leftStick != None:
                    current_value = current_value.leftStick
                return current_value
            #case 3: There are two ongoing sticks from our branch, replace the branch with the right, or left to the right branch, and recursivly delete that
            if how_many_sticks(branch) == 2:
                branch_succesor = give_smallest_stick(branch.rightStick)
                branch.value = branch_succesor.value
                self.get_rid_rec(branch_succesor)