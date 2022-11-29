from collections import defaultdict

def answer():
# space complexity = O(N) where N is the number of words belonging to group A
# Time Complexity = O(M*Q) Where M is the words belonging to group B and Q is the most repeating word in Group A
    try:
        N , M = map(int,input().split())
        A_dictionary = defaultdict(list)

        #Loop N times to get the A group elements    
        for i in range(N):
            word = input()
            A_dictionary[word].append(i+1) # as i starts from 0

        #Loop M * Q times to get the B group elements (M), and (Q) is the size of the list contains the indexes of each word
        for i in range(M):
            word = input()
            if A_dictionary[word]==[]:
                print(-1)
            else:
                print(*A_dictionary[word])  # it takes O(Q) Where Q is the size of the list
    except:
        answer()

        
if __name__ == '__main__':
    answer()