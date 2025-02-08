class DirectedGraph:
    def __init__(self):
        """ایجاد گراف جهت‌دار"""
        self.graph = {}

    def add_event(self, event_name):
        if event_name not in self.graph:
            self.graph[event_name] = []

    def add_dependency(self, event_a, event_b):
        """افزودن وابستگی بین دو رویداد"""
        if event_a in self.graph and event_b in self.graph:
            self.graph[event_a].append(event_b)

    def has_cycle(self):
        """تشخیص وجود چرخه در گراف"""
        visited = set()
        stack = set()

        def dfs(node):
            if node in stack:
                return True
            if node in visited:
                return False
            visited.add(node)
            stack.add(node)
            for neighbor in self.graph.get(node, []):
                if dfs(neighbor):
                    return True
            stack.remove(node)
            return False

        for node in self.graph:
            if dfs(node):
                return True
        return False
