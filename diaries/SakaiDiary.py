from diaries.AbstractDiary import AbstractDiary

class SakaiDiary(AbstractDiary):

    def get_date(self):
        return "2022-12-04"

    def get_summary(self):
        return "大講義室が寒い。暖房を効かしてほしい。出来ることなら寝転がるだけで単位がほしい。"

    def get_author(self):
        return "H.Sakai"