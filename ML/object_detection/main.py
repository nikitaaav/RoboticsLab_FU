import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

img_dir_path = 'pic_1.jpg'
result = model(img_dir_path)

result.show()
# result.print() - вывести данные
# result.save() - сохранить в файл
# object_count = len(result.pandas().xyxy[0]) - данные о всех найденных объектах на фото
# print(result.pandas().xyxy[0]['name']) - вывод таблицы объект-количество его на фото

count_person = 0
for i in result.pandas().xyxy[0]['name']:
    if i == 'person':
        count_person += 1

print(count_person)