class MinHeap:
    def __init__(self):
        """ایجاد صف اولویت"""
        self.heap = []

    def insert(self, event):
        """افزودن رویداد به صف اولویت"""
        self.heap.append(event)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """حذف و بازگرداندن کم‌اولویت‌ترین رویداد"""
        if len(self.heap) == 0:
            return None
        self._swap(0, len(self.heap) - 1)
        min_event = self.heap.pop()
        self._heapify_down(0)
        return min_event

    def peek(self):
        """مشاهده کم‌اولویت‌ترین رویداد"""
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    


    def _compare(self, event1, event2):
        if event1.priority == event2.priority:
            return event1.date < event2.date  # مقایسه تاریخ
        return event1.priority < event2.priority  # تصحیح خطا

    def _heapify_up(self, index):
        while index > 0 and self._compare(self.heap[index], self.heap[(index - 1) // 2]):
            self._swap(index, (index - 1) // 2)
            index = (index - 1) // 2

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self._compare(self.heap[left], self.heap[smallest]):
            smallest = left
        if right < len(self.heap) and self._compare(self.heap[right], self.heap[smallest]):
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
