class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}

        def dfs(current):
            if current in old_to_new:
                return old_to_new[current]

            copy = Node(current.val)
            old_to_new[current] = copy

            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node) if node else None