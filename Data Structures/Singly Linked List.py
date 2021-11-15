class Node:
    	def __init__(self, data):
		    self.data = data
		    self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def display(self):
		if(self.head):
			temp_node = self.head
			while(temp_node != None):
				if(temp_node.next != None):
					print(temp_node.data, " -> ", end=" ")
				else:
					print(temp_node.data, end=" ")
				temp_node = temp_node.next
		else:
			print("\nEmpty Linked List!")

	def insert_beg(self, new_node):
		if(self.head):
			new_node.next = self.head
			self.head = new_node
		else:
			self.head = new_node

	def insert_end(self, new_node):
		if(self.head):
			last_node = self.head
			while(last_node.next != None):
				last_node = last_node.next
			last_node.next = new_node
		else:
			self.head = new_node

	def insert_nth(self, n, new_node):
		if(self.head):
			if(n == 1):
				self.insert_beg(new_node)
			else:
				n = n - 1
				temp_node = self.head
				while(n>1):
					temp_node = temp_node.next
					n = n - 1
				new_node.next = temp_node.next
				temp_node.next = new_node
		else:
			print("\nEmpty Linked List!")

	def delete_beg(self):
		if(self.head):
			self.head = self.head.next
		else:
			print("\nEmpty Linked List!")

	def delete_end(self):
		if(self.head):
			if(self.head.next == None):
				self.head = None
			else:
				temp_node = self.head
				while(temp_node.next.next != None):
					temp_node = temp_node.next
				temp_node.next = None
		else:
			print("\nEmpty Linked List!")

	def delete_nth(self, n):
		if(self.head):
			if(n == 1):
				self.delete_beg()
			else:
				del_next_node = self.head
				n = n - 1
				while(n>1):
					del_next_node = del_next_node.next
					n = n - 1
				del_next_node.next = del_next_node.next.next
		else:
			print("\nEmpty Linked List!")

	def delete_val(self, val):
		if(self.head):
			if(self.head.data == val):
				self.delete_beg()
			else:
				flag = False
				del_next_node = self.head
				while(del_next_node != None):
					if(del_next_node.next.data == val):
						flag = True
						break
					del_next_node = del_next_node.next
				if(flag == False):
					print("\nValue not found in linked list!")
				else:
					del_next_node.next = del_next_node.next.next
		else:
			print("\nEmpty Linked List!")

	
   
LL = LinkedList()

print("\n1. Insert Beginning\n2. Insert End\n3. Insert n'th\n4. Delete Beginning\n5. Delete End\n6. Delete n'th element\n7. Delete value\n8. Display\n9. Exit")
ch = 0
while(ch != 9):
	ch = int(input("\nEnter choice: "))
	if(ch == 1):
		v = int(input("\nEnter value: "))
		LL.insert_beg(Node(v))
	elif(ch == 2):
		v = int(input("\nEnter value: "))
		LL.insert_end(Node(v))
	elif(ch == 3):
		v = int(input("\nEnter value: "))
		n = int(input("\nEnter position: "))
		LL.insert_nth(n, Node(v))
	elif(ch == 4):
		LL.delete_beg()
	elif(ch == 5):
		LL.delete_end()
	elif(ch == 6):
		n = int(input("\nEnter value: "))
		LL.delete_nth(n)
	elif(ch == 7):
		val = int(input("\nEnter value: "))
		LL.delete_val(val)
	elif(ch == 8):
		LL.display()
	elif(ch == 9):
		exit()
	else:
		print("\nInvalid choice!")	
