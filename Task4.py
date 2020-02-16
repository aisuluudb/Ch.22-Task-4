from datetime import timedelta

timestamp1 = timedelta(hours=6,minutes=1,seconds=30)
timestamp2 = timedelta(hours=6,minutes=2,seconds=10)
time = timestamp2-timestamp1
print(time)