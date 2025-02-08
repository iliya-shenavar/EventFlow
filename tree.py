class TreeNode:
    def __init__(self, event):
        """
        گره‌ای که یک رویداد را نگه می‌دارد
        :param event: شیء رویداد
        """
        self.event = event
        self.left = None
        self.right = None


class EventTree:
    def __init__(self):
        """ایجاد یک درخت خالی برای دسته‌بندی رویدادها"""
        self.root_by_date = None
        self.root_by_participants = None
        self.root_by_instructor = None

    def insert_by_date(self, event):
        """افزودن رویداد به درخت بر اساس تاریخ برگزاری"""
        self.root_by_date = self._insert_recursive(self.root_by_date, event, key=lambda e: e.date)

    def insert_by_participants(self, event):
        """افزودن رویداد به درخت بر اساس تعداد شرکت‌کنندگان"""
        self.root_by_participants = self._insert_recursive(self.root_by_participants, event, key=lambda e: len(e.participants))

    def insert_by_instructor(self, event):
        """افزودن رویداد به درخت بر اساس نام مدرس"""
        self.root_by_instructor = self._insert_recursive(self.root_by_instructor, event, key=lambda e: e.instructor)

    def _insert_recursive(self, node, event, key):
        """تابع بازگشتی برای افزودن گره به درخت"""
        if node is None:
            return TreeNode(event)
        if key(event) < key(node.event):
            node.left = self._insert_recursive(node.left, event, key)
        elif key(event) > key(node.event):
            node.right = self._insert_recursive(node.right, event, key)
        return node

    def inorder_by_date(self):
        """بازگرداندن لیست مرتب‌شده رویدادها بر اساس تاریخ"""
        events = []
        self._inorder_recursive(self.root_by_date, events)
        return events

    def inorder_by_participants(self):
        """بازگرداندن لیست مرتب‌شده رویدادها بر اساس تعداد شرکت‌کنندگان"""
        events = []
        self._inorder_recursive(self.root_by_participants, events)
        return events

    def inorder_by_instructor(self):
        """بازگرداندن لیست مرتب‌شده رویدادها بر اساس نام مدرس"""
        events = []
        self._inorder_recursive(self.root_by_instructor, events)
        return events

    def _inorder_recursive(self, node, events):
        """تابع بازگشتی برای پیمایش درخت به صورت مرتب (in-order)"""
        if node is not None:
            self._inorder_recursive(node.left, events)
            events.append(node.event)
            self._inorder_recursive(node.right, events)

    def __str__(self):
        """نمایش رویدادهای مرتب‌شده به صورت خوانا"""
        events_by_date = self.inorder_by_date()
        return "\n".join([f"{event.name} - {event.date}" for event in events_by_date])
