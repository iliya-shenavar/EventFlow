class Event:
    def __init__(self, name, date, priority, instructor=None):
        """
        کلاس مدیریت رویداد
        :param name: نام رویداد
        :param date: تاریخ برگزاری
        :param priority: اولویت رویداد
        :param instructor: نام مدرس
        """
        self.name = name
        self.date = date
        self.priority = priority
        self.instructor = instructor
        self.participants = []
        self.state = "Not Started"  # وضعیت پیش‌فرض
        self.rating = None  # امتیاز رویداد

    def add_participant(self, participant):
        """افزودن شرکت‌کننده به رویداد"""
        if participant not in self.participants:
            self.participants.append(participant)
            return f"Participant '{participant}' successfully added to '{self.name}'."
        return f"Participant '{participant}' is already registered for '{self.name}'."

    def remove_participant(self, participant):
        """حذف شرکت‌کننده از رویداد"""
        if participant in self.participants:
            self.participants.remove(participant)
            return f"Participant '{participant}' removed from '{self.name}'."
        return f"Participant '{participant}' is not registered for '{self.name}'."

    def update_state(self, new_state):
        """به‌روزرسانی وضعیت رویداد"""
        valid_states = ["Not Started", "Ongoing", "Completed"]
        if new_state in valid_states:
            self.state = new_state
            return f"Event '{self.name}' state updated to '{self.state}'."
        return "Invalid state. Valid states: Not Started, Ongoing, Completed."

    def rate_event(self, rating):
        """امتیازدهی به رویداد"""
        if 1 <= rating <= 5:
            self.rating = rating
            return f"Event '{self.name}' rated {self.rating} out of 5."
        return "Rating must be between 1 and 5."

    def __str__(self):
        return f"Event(Name: {self.name}, Date: {self.date}, Priority: {self.priority}, " \
               f"State: {self.state}, Participants: {len(self.participants)})"
