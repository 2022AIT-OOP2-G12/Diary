from diaries.AbstractDiary import AbstractDiary

class Nakashima150Diary(AbstractDiary):

    def get_date(self):
        return "2022-12-10"

    def get_summary(self):
        return "のんびりした休日を過ごした"

    def get_author(self):
        return "中島"