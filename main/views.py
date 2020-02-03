from django.shortcuts import render


f = open("static\data.csv", 'r', encoding='cp949')
# unicode, cp949, utf-8 셋 중에 하나로 인코딩해서 안되면 그때부터 좀 복잡해짐
l = []
lines = f.readlines()
for line in lines:
    l.append(line.split(','))
f.close()
data = l[1:300]

def index(request):

    return render(request, 'main/index.html', {'data':data})
