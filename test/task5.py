class DoublyLinkedList:
    def __init__(self, data):
        self.value = data
        self.prev_node_ref = None
        self.next_node_ref = None
       

class DoublyLinkedListFunctions:
    def __init__(self):
        self.start_node = None
        self.end_node = None


    def push(self, data): # add value to the end of the list
        new_node = DoublyLinkedList(data)
        if(self.start_node == None):
            self.start_node = self.end_node = new_node
            self.start_node.prev_node_ref = None
            self.end_node.next_node_ref = None
        else:
            self.end_node.next_node_ref = new_node
            new_node.prev_node_ref = self.end_node
            self.end_node = new_node
            self.end_node.next_node_ref = None

    
    def pop(self): # remove value from the end of the list
        if(self.start_node == None):
            return
        else:
            if(self.start_node != self.end_node):   
                self.end_node = self.end_node.prev_node_ref
                self.end_node.next_node_ref = None
            else:   
                self.start_node = self.end_node = None
                   
    
    def shift(self): # remove value at the beginning of the list
        if(self.start_node == None):
            return
        else:
            if(self.start_node != self.end_node):
                self.start_node = self.start_node.next_node_ref
                self.start_node.prev_node_ref = None
            else:
                self.start_node = self.end_node = None
                   

    def nshift(self, data): # write the value to the beginning of the list
        new_node = DoublyLinkedList(data)
        if(self.start_node == None):
            self.start_node = self.end_node = new_node
            self.start_node.prev_node_ref = None
            self.end_node.next_node_ref = None
        else:
            self.start_node.prev_node_ref = new_node
            new_node.next_node_ref = self.start_node
            new_node.prev_node_ref = None
            self.start_node = new_node

             
    def display_result(self):
        current = self.start_node
        if(self.start_node == None):
            print("List is empty")
            return
        while(current != None):   
            print(current.value) 
            current = current.next_node_ref     
        print()


funcs_list = DoublyLinkedListFunctions()    
funcs_list.push(1)
funcs_list.push(2)
funcs_list.push(3)
funcs_list.push(4)
funcs_list.push(5) 
funcs_list.display_result()

funcs_list.pop()
funcs_list.display_result()

funcs_list.shift()
funcs_list.display_result()

funcs_list.nshift(45)
funcs_list.nshift(54)
funcs_list.display_result()