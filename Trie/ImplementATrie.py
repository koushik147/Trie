class TrieNode:
    def __init__(self):
        self.isEnd = False # creating the isend value to false
        self.children = [None]*26 # creating the children array with None value for 26 space
class Trie(object):

    def __init__(self):
        self.root = TrieNode() # creating the trienode and setting it to root
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root # setting root to current
        for char in word:
            key = ord(char) - ord('a') # finding the key value by subtracting the ascii value of char and 'a'
            if curr.children[key]==None: # if key is not equal to None
                curr.children[key]= TrieNode() # then create the trienode and assign it to current of children
            curr = curr.children[key] # assign the key value to current 
        curr.isEnd = True # assign the current is end to True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root # setting root to current
        for char in word:
            key = ord(char)-ord('a') # finding the key value by subtracting the ascii value of char and 'a'
            if curr.children[key]==None: # if key is not equal to None the return false
                return False
            curr = curr.children[key] # assign the key value to current 
        return curr.isEnd # return the isend

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root # setting root to current
        for char in prefix:
            key = ord(char) - ord('a') # finding the key value by subtracting the ascii value of char and 'a'
            if curr.children[key]==None: # if key is not equal to None the return false
                return False
            curr = curr.children[key] # assign the key value to current then return true
        return True
        