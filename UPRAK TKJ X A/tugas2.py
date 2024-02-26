belanja =[ 
    {"siswa":"1","nilai":85},    
    {"siswa":"2","nilai":90},
    {"siswa":"3","nilai":78}, 
    {"siswa":"4","nilai":92}, 
    {"siswa":"5","nilai":88},   
    ]

nilai_sering = 0
for item in belanja :
        nilai_sering += item ["nilai"]

print("nilai sering :",nilai_sering)