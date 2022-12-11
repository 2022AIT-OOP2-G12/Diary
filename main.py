from diaries.DiarySample import DiarySample
from diaries.SakaiDiary import SakaiDiary
from diaries.Nakashima150Diary import Nakashima150Diary
from diaries.OnodaDiary import OnodaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    SakaiDiary(),
    Nakashima150Diary(),
    OnodaDiary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()