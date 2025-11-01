from collections import defaultdict
def group_anagrams(strs: list[str]) -> list[list[str]]:
    anag_dict = defaultdict(list)
    for i in strs:
        count = [0] * 26
        for c in i:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)
        anag_dict[key].append(i)
    return anag_dict.values()

if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))