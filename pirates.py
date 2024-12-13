from random import*

class Pirates:
    names = {}              #словарь пиратов
    count=4                 #колтчесьво пиратов
    start_from=1            #начало отсчета ключей
    template='pirate_%d'    #шаблон названия  ключей
    def values(self):     #конструктор для создания имен пиратов
        for i in range(self.start_from,self.count+self.start_from):#цикл для добавления self.count которые начинаются с self.start_from
            self.names[self.template%i] = input() # добавление в словарь имен пиратов

    def get_names(self):# метод для возвращения имен пиратов
        return self.names

class Ships:
    weights={}
    count=4
    start_from = 1
    template = 'ship_%d'
    def values(self):
        for i in range(self.start_from,self.count+self.start_from):
            self.weights[self.template % i] = int(input())

    def get_names(self):# метод для возвращения имен пиратов
        return self.weights

class Box:
    collection={}
    template_collection='box_%d'

    count=60
    start_from=4

    def load_collection(self):
        for i in range(self.start_from,self.count+1):
            box={}
            item=self.get_item()
            if item=='деньги':
                box={"weight":randint(4,10),"content":item,"count":randint(15, 100)}
            if item=='пусто':
                box = {"weight": 1, "content": item }
            if item=='проклятье':
                box = {"weight": randint(4, 10), "content": item,"count":randint(3, 10)}
            self.collection[self.template_collection%i]=box

    def get_collection(self):
        return self.collection

    def has_item(self):
        return randint(0,1)>0

    def get_item(self):
        if self.has_item():
            if self.has_cash():
                return 'деньги'
            if self.has_curse():
                return 'проклятье'

        return 'пусто'

    def has_cash(self):
        return randint(0, 1) > 0

    def has_curse(self):
        return randint(0, 1) > 0

    def get_boxes_by_weight(self,ship_weight):
        count=0
        gold=0
        empty=0
        curse=0
        for box in self.collection.copy():

            box_weight=self.collection.setdefault(box).setdefault('weight')#ищем вес ящика по ключу
            box_content=self.collection.setdefault(box).setdefault('content')#ищем вес ящика по ключу

            if (ship_weight-box_weight)>0:#проверяем что мы можем взять ящик
                if box_content == 'деньги':
                    box_count= self.collection.setdefault(box).setdefault('count')
                    gold+=box_count
                if box_content == 'пусто':
                    empty += 1
                if box_content == 'проклятье':
                    box_count = self.collection.setdefault(box).setdefault('count')
                    curse+=box_count
                count+=1#считаем ящики
                ship_weight=ship_weight-box_weight
                self.collection.pop(box)#удаляем из колекции взятый ящик
            else:
                continue
        print('вес оствточный коробля',ship_weight)
        return {"count":count,"gold":gold,"curse":curse,"empty":empty}

pirates=Pirates()

ships=Ships()

box=Box()
box.load_collection()
print(box.get_collection())

pirates.values()

ships.values()

print(pirates.get_names())
print(ships.get_names())
result={}
for i in ships.get_names():
    ships_weight = ships.get_names().setdefault(i)
    print('вес коробля', ships_weight)
    # print('сколько взял корабаль %s'%i,box.get_boxes_by_weight(ships_weight))
    result[i]=box.get_boxes_by_weight(ships_weight)

def sort_by_key(data, nested_key, reverse=False):
    return sorted(data.keys(), key=lambda k: data[k][nested_key], reverse=reverse)

# sorted_keys = sort_dict_by_nested_key(data, 'gold', reverse=True)
# print(sorted_keys)

print(result)
print('gold')
max_gold=sort_by_key(result,'gold',reverse=True)[0]
print(max_gold)
max_gold_count=result.setdefault(max_gold).setdefault('gold')
print(max_gold_count)
print('curse')
max_curse=sort_by_key(result,'curse',reverse=True)[0]
print(max_gold)
max_curse_count=result.setdefault(max_curse).setdefault('curse')
print(max_curse_count)
print('empty')
min_empty=sort_by_key(result,'empty')[0]
print(min_empty)
min_empty_count=result.setdefault(min_empty).setdefault('empty')
print(min_empty_count)
