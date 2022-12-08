from diaries.AbstractDiary import AbstractDiary

class NishidaDiary(AbstractDiary):

    def get_date(self):
        return "2022-12-09"

    def get_summary(self):
        return "今日はオブジェクト指向ぷログラミングのグループワークだった。"

    def get_author(self):
        return "ニシダタクマ"