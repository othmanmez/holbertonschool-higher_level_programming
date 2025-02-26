class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")
    
    def extend(self, iterable):
        items_count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {items_count} items.")
    
    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)

# Testing the VerboseList
verbose_list = VerboseList([1, 2, 3])

verbose_list.append(4)
verbose_list.extend([5, 6])
verbose_list.remove(3)
verbose_list.pop()
verbose_list.pop(0)
