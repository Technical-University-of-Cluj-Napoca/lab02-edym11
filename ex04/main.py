from BST import BST
from search_engine import search_loop
if __name__ == "__main__":
    # bst = BST("https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words.txt", url = True)
    bst = BST("wordlist.txt", file = True)
    # matches = bst.autocomplete("cat")
    # print(matches[:10])

    search_loop(bst)
