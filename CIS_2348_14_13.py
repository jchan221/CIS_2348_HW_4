num_calls = 0

def partition(user_ids, low, high):
    i_index = (low - 1)
    pivot = user_ids[high]
    
    for j in range(low , high):
        if user_ids[j] <= pivot:
            i_index = i_index + 1
            user_ids[i_index],user_ids[j] = user_ids[j],user_ids[i_index]
            user_ids[i_index + 1],user_ids[high] = user_ids[high],user_ids[i_index + 1]
    return(i_index + 1)
# The function above will compare the last string with the other elements and if it is small will increment by 1
def quicksort(user_ids, i, k):
    global num_calls
    num_calls = num_calls + 1
    if i < k:
        pi = partition(user_ids,i,k)
        quicksort(user_ids,i,pi - 1)
        num_calls = num_calls + 1
        quicksort(user_ids,pi + 1,k)
# the method will increment num_calls everytime it is called, and will sort the elements alphabetically
if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
        
    # Initial call to quicksort 
    quicksort(user_ids, 0, len(user_ids) - 1)
    
    # Print number of calls to quicksort
    print(num_calls)
    
    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
