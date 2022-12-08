from diaries.DiarySample import DiarySample
from diaries.Alfarcats_diary import Alfarcats_diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    Alfarcats_diary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()