class Node():
    def __init__(self, data, nextNode= None):
        self.data=data
        self.nextNode=nextNode


class LinkedList():
    def __init__(self, head= None ):
        self.head=head
    def add(self, value):
        newNode= Node(value)

        if self.head==None:
            self.head=newNode
            return
        current_node=self.head
        while (1):
            if  current_node.nextNode==None:
                current_node.nextNode=newNode
                break
            current_node=current_node.nextNode
    def print_list(self):
        current_node=self.head
        while(current_node!=None):
            print current_node.data,"->",
            current_node=current_node.nextNode
    def delete(self,index=0):
        current_node=self.head
        index_counter=0;

        if index==0:
            self.head=current_node.nextNode
            return

        while(1):
            if index_counter==index-1:
                  previous_node=current_node
            if index_counter==index:
                upcoming_node=current_node.nextNode
                current_node=previous_node
                current_node.nextNode=upcoming_node
                break
            current_node=current_node.nextNode
            index_counter+=1

    def access_element(self, index):

        current_node=self.head
        index_counter=0;

        while (index!= index_counter):
            index_counter+=1
            current_node=current_node.nextNode
        return current_node.data

    def size(self):
        current_node=self.head
        size_counter=1
        while(current_node.nextNode != None):
            current_node=current_node.nextNode
            size_counter+=1
    def insert (self, data, index):

        current_node=self.head
        index_counter=0
        while True:
            if index_counter == index-1:
                previous_node=current_node
            if index_counter== index:
                newNode=Node(data,current_node)
                current_node=previous_node
                current_node.nextNode=newNode
                break
            current_node=current_node.nextNode
            index_counter+=1




