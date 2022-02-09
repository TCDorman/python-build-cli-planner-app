class PrefixedReminder:
    """This class acts as a base class for other types of reminders.
    Classes that subclass it should override the `self.text` property
    """
    def __init__(self, prefix="Hey, don't forget to "):
        self.prefix = prefix
        self.text = prefix + '<placeholder_text>'

class PoliteReminder(PrefixedReminder):
    """Tis class inerits from Prefixed Reminder. Its __init__() should 
    accept a text parameter; for now you don't need to use it. Initiate 
    the parent class by calling super().__init__() with a polite prefix 
    (the prefix should contain the word "please").
    """
    def __init__(self, text):
        super().__init__(prefix="please remember to ")
        self.text = self.prefix + text
