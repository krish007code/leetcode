class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_seen = []
        matrix = []
        for i in strs:
            if tuple(sorted(i)) in sorted_seen:
                index = sorted_seen.index(tuple(sorted(i)))
                matrix[index].append(i)
            else:
                sorted_seen.append(tuple(sorted(i)))
                matrix.append([i])
        return matrix