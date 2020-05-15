'''Implement a Python program to generate all sentences where subject is in ["Americans",
"Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].'''
subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]
sentence_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
    print (sentence)