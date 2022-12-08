from diaries.DiarySample import DiarySample
from diaries.Nakashima150Diary import Nakashima150Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    Nakashima150Diary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()