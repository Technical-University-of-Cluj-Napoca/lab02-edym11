from urllib import request
class Node:
    def __init__(self, word : str):
        self.word = word
        self.left = None
        self.right = None

class BST:
    def __init__(self, source: str, **kwargs):
        self.source = source
        isUrl = False
        for k, val in kwargs.items():
            if k == "url":
                isUrl = val
        if isUrl:
            response = request.urlopen(self.source)
            data = response.read()
            text = data.decode('utf-8')
            words = text.splitlines()
            self.root = self._build_tree(words)
        else:
            with open(self.source, 'r', encoding='utf-8') as f:
                words = f.read().splitlines()
            self.root = self._build_tree(words)
    def _build_tree(self, words: list):
        if len(words) == 0:
            return None
        mid = len(words) // 2
        node = Node(words[mid])
        node.left = self._build_tree(words[:mid])
        node.right = self._build_tree(words[mid + 1:])
        return node
    def _collect(self, node: Node, prefix: str, result) -> None:
        if node == None:
            return
        self._collect(node.left, prefix, result)
        if node.word[:len(prefix)] == prefix:
            result.append(node.word)
        self._collect(node.right, prefix, result)
    def autocomplete(self, prefix: str) -> list[str]:
        result = []
        self._collect(self.root, prefix, result)
        return result
