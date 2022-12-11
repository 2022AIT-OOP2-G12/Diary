from diaries.AbstractDiary import AbstractDiary

class OnodaDiary(AbstractDiary):

    def get_date(self):
        return "2022-12-04"

    def get_summary(self):
        return "気温が一気に下がり寒い一日だった"

    def get_author(self):
        return "小野田"