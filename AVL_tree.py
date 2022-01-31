class Branch:
    def __init__(self, value):
        self.value = value
        self.leftStick = None
        self.rightStick = None
        self.times = 1 
        self.elderStick = None
        self.height = 1


class AVL_tree:
    def __init__(self):
        self.root = None

    def creator(self, listed =[]):
        for i in listed:
            self.insert(i)

    def destructor(self, listed=[]):
        for i in listed:
            self.get_rid(i)

    def get_height(self, now_branch):
        if now_branch == None:
            return 0
        else:
            return now_branch.height
            
    def higher_stick(self, now_branch):
        right = self.get_height(now_branch.rightStick)
        left = self.get_height(now_branch.leftStick)
        if left >= right:
            return now_branch.leftStick
        else:
            return now_branch.rightStick

    def insert(self, number):
        if self.root==None:
            self.root = Branch(number)
        else: 
            self.deep_insert(number, self.root)

    def deep_insert(self,number,now_branch ):
            if number < now_branch.value:
                if now_branch.leftStick == None:
                    now_branch.leftStick = Branch(number)
                    now_branch.leftStick.elderStick = now_branch
                    self.inspection_insert(now_branch.leftStick)
                else:
                    self.deep_insert(number, now_branch.leftStick, )
            elif number > now_branch.value:
                if now_branch.rightStick == None:
                    now_branch.rightStick = Branch(number)
                    now_branch.rightStick.elderStick = now_branch
                    self.inspection_insert(now_branch.rightStick)
                else:
                    self.deep_insert(number, now_branch.rightStick)
            else:
                now_branch.times = now_branch.times + 1
                #print("The number:" + str(number) + " occured " + str(now_branch.times))

    def print(self):
         if self.root != None:
            self.rec_print(self.root)

    def rec_print(self, now_branch):
        if now_branch != None:
            self.rec_print(now_branch.leftStick)
            #print ((str(now_branch.value),now_branch.height))
            self.rec_print(now_branch.rightStick)
        
    def find_branch(self, value):
        if self.root != None:
            return self.find_value(value, self.root)
        else:
            return None
    
    def find_value(self, value, now_branch):
        if value == now_branch.value:
            return now_branch
        elif value < now_branch.value and now_branch.leftStick != None:
            return self.find_value(value, now_branch.leftStick)
        elif value > now_branch.value and now_branch.rightStick !=None:
            return self.find_value(value, now_branch.rightStick)

    def get_rid(self, value):
        return self.get_rid_rec(self.find_branch(value))

    def get_rid_rec(self, branch):
        if branch ==None or self.find_branch(branch.value) == None:
            return None

        if branch.times > 1:
            #print("remaining:" + str(branch.times))
            branch.times = branch.times -1
        else:
            def how_many_sticks(branch):
                num_sticks = 0
                if branch.leftStick != None:
                    num_sticks = num_sticks + 1
                if branch.rightStick != None:
                    num_sticks = num_sticks + 1
                return num_sticks

            if how_many_sticks(branch) == 0:
                if branch.elderStick != None:
                    if branch.elderStick.leftStick == branch:
                        branch.elderStick.leftStick = None
                    else:
                        branch.elderStick.rightStick = None
                else:
                    self.root = None

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

            if how_many_sticks(branch) == 2:
                branch_succesor = give_smallest_stick(branch.rightStick)
                branch.value = branch_succesor.value
                self.get_rid_rec(branch_succesor)
                return

            if branch.elderStick != None:
                branch.elderStick.height = max(self.get_height(branch.elderStick.rightStick),
                self.get_height(branch.elderStick.leftStick)) + 1

                self.inspection_delete(branch.elderStick)

    def inspection_insert(self, now_branch, road = []):
        if now_branch.elderStick == None: 
            return 
        road = [now_branch] + road
        left_stick_height = self.get_height(now_branch.elderStick.leftStick)
        right_stick_height = self.get_height(now_branch.elderStick.rightStick)

        if abs(right_stick_height - left_stick_height)>1:
            road = [now_branch.elderStick] + road
            self.rebalance_branches(road[0],road[1],road[2])
            return
        height_new = now_branch.height +1
        if height_new > now_branch.elderStick.height:
            now_branch.elderStick.height = height_new

        self.inspection_insert(now_branch.elderStick, road)

    def inspection_delete(self, now_branch):
        if now_branch == None:
            return

        left_stick_height = self.get_height(now_branch.leftStick)
        right_stick_height = self.get_height(now_branch.rightStick)

        if abs(right_stick_height - left_stick_height)>1:
            y = self.higher_stick(now_branch)
            x = self.higher_stick(y)
            self.rebalance_branches(now_branch, y, x)

        self.inspection_delete(now_branch.elderStick)

    def rebalance_branches(self,z,y,x):
        if y==z.rightStick and x==y.leftStick:
            self.rotate_to_right(y)
            self.rotate_to_left(z)

        elif y ==z.rightStick and x== y.rightStick:
            self.rotate_to_left(z)
        elif y==z.leftStick and x==y.rightStick:
            self.rotate_to_left(y)
            self.rotate_to_right(z)

        elif y==z.leftStick and x==y.leftStick:
            self.rotate_to_right(z)
        else:
            raise Exception('rebalance_branches:Something is wrong with the configuration of the branches')
        


    def rotate_to_right(self,z):
        sub_root = z.elderStick
        y = z.leftStick
        t3 = y.rightStick
        y.rightStick = z
        z.elderStick = y
        z.leftStick = t3
        if t3 != None:
            t3.elderStick = z
        y.elderStick = sub_root
        if y.elderStick == None:
            self.root = y
        else: 
            if y.elderStick.leftStick ==z:
                y.elderStick.leftStick =y
            else:
                y.elderStick.rightStick = y
        z.height = max(self.get_height(z.leftStick),
        self.get_height(z.rightStick)) +1
        y.height = max(self.get_height(y.leftStick),
        self.get_height(y.rightStick)) + 1


    def rotate_to_left(self, z):
        sub_root = z.elderStick
        y = z.rightStick
        t2 = y.leftStick
        y.leftStick = z
        z.elderStick = y
        z.rightStick =t2
        if t2 != None:
            t2.elderStick = z
        y.elderStick = sub_root
        if y.elderStick == None:
            self.root = y
        else: 
            if y.elderStick.leftStick ==z:
                y.elderStick.leftStick =y
            else:
                y.elderStick.rightStick = y
        z.height = max(self.get_height(z.leftStick),
        self.get_height(z.rightStick)) +1
        y.height = max(self.get_height(y.leftStick),
        self.get_height(y.rightStick)) + 1

