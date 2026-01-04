pass_fail = []
Avg = [90,80,50,30,85,70,69]
pass_threshold  = 50
for score in Avg:
    if score  >= pass_threshold: 
       pass_fail.append(True)
    else:
        pass_fail.append(False)


for i, status in enumerate(pass_fail):
    if status:
        print(f"Students {i+1}: Pass")
    else:
        print(f"students {i+1}: Fail")

for i, (score, status) in enumerate(zip(Avg, pass_fail)):
    if status:
        print(f"Student {i+1}: Score - {score}, Result - Pass")
    else:
        print(f"Student {i+1}: Score - {score}, Result - Fail")
