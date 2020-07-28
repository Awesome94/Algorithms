def reverse_linked_list(head):
    nodes = []
    while head:
        nodes.append(head)
        head = head.next
    while nodes:
        print(nodes.pop())
