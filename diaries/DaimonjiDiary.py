from diaries.AbstractDiary import AbstractDiary
class DaimonjiDiary(AbstractDiary):

    
        def get_date(self):
            return "2020-11-18"
    
        def get_summary(self):
            return "今日は、実験で、脳波を計測した。"
    
        def get_author(self):
            return "Daimonji"