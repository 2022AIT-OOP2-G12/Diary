from diaries.AbstractDiary import AbstractDiary

class Alfarcats_diary(AbstractDiary):

    def get_date(self):
        return "2022-12-01"

    def get_summary(self):
        return "大変な日だった"

    def get_author(self):
        return "さとう"