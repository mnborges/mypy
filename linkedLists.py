class node:
    def __init__ (self, data = None):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = node()
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    def length(self):
        total = 0
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            total += 1
        return total
    def display(self):
        elems =[]
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print ('ITEMS IN LIST: ', elems)
    def get(self,index):
        if index >= self.length():
            print('Index out of range')
            return None
        cur = self.head
        pos = 0
        while pos != index+1:
            cur = cur.next
            pos +=1
        return cur.data    
    def erase(self, index):
        if index >= self.length():
            print('Index out of range')
            return None
        cur_index = 0
        cur_node = self.head
        while cur_index < self.length():
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index+=1
    def deleteDuplicate(self): #it only deletes copies
        cur = self.head
        flag = 0
        index = 0
        li_idx= []
        while cur.next != None:
            if not (flag): 
                last = cur
            cur = cur.next
            if (flag and last.data != cur.data):
                print('.')
            flag = 0
            if last.data == cur.data:
                last.next = cur.next
                li_idx.append(index)
                index-=1
                flag = 1
            if (flag and cur.next == None):
                print('.')
            index+=1
        print('INDEXES : ' , li_idx)
    def deleteAllDuplicate(self): #it deletes all numbers that have duplicates
        flag =0
        cur_node = self.head
        fst_node = cur_node
        while cur_node.next != None:
            if not flag: prev_node = cur_node
            cur_node = cur_node.next
            if prev_node.data == cur_node.data:
                prev_node.next = cur_node.next
                flag = 1
                if cur_node.next == None: fst_node.next = prev_node.next
            else: 
                if flag:
                    fst_node.next = prev_node.next
                    flag =0
                else: fst_node = prev_node
            #print('Current node: ', cur_node.data, '- Previous node: ', prev_node.data, '- First node: ' , fst_node.data )
my_list = linked_list()
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(5)
my_list.append(5)
my_list.append(5)
my_list.append(5)
my_list.append(6)
my_list.append(7)
my_list.append(7)
my_list.append(7)
my_list.display()
my_list.deleteAllDuplicate()
print('************************')
my_list.display()
#print('************************')
#print(my_list.get(0))
#my_list.erase(0)
#my_list.display()