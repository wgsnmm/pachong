import json

data = [
    {
        'name':'呵呵',
        'gender':'male',
        'birthday':'1992-10-18'
    },{
        'name':'啥子',
        'gender':'male',
        'birthday':'1996-10-18'
    }
]
with open('data.josn','w',encoding='utf-8') as file:
    file.write(json.dumps(data,indent=2,ensure_ascii=False))