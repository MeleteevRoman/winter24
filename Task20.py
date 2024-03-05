#Задача 21-1
import pandas as pd

dct={'Год обучения':[2021,2022,2023,2024,2025],
     'Кол-во часов':['56ч','56ч','57ч','58ч','59ч'],
     'Размер гр.':[20,20,25,25,30],
     'Факт. размер':[13,20,17,14,18],
     'Цена':[54,54,55,56,56],
     'Преподователь':['Иванов','Иванов','Иванов','Петров','Сидоров'],
     }
Pupil=pd.DataFrame(dct)
print(Pupil)
print(Pupil.columns)
print(list(Pupil))

#Задача 20-2



#Задача 20-3
CREATE TABLE book1(book_id int,book_title text,book_author text,publisher_id int)
INSERT INTO book1 VALUES
(1,'Мастер и Маргарита','Булгаков',1),
(2,'Бег','Булгаков',1),
(3,'Роковые яйца','Булгаков',1),
(4,'Мцыри','Лермонтов',2),
(5,'Бордино','Лермонтов',2),
(6,'Война и мир','Толстой',3),
(7,'Анна Каренина','Толстой',3),
(8,'Кавказский пленник','Толстой',3),
(9,'Вий','Гоголь',4),
(10,'Ревизор','Гоголь',4),
(11,'Шинель','Гоголь',4),
(12,'Преступление и наказание','Достоевский',5),
(13,'Братья Карамазовы','Достоевский',5),
(14,'Бесы','Достоевский',5)

SELECT * FROM book1
SELECT * FROM book1 WHERE book_id>5
SELECT * FROM book1 WHERE book_author like 'Т%'
SELECT * FROM book1 WHERE book_author like '%в'
SELECT * FROM book1 WHERE book_title like 'М%'
SELECT * FROM book1 WHERE book_title like 'Б%'
SELECT * FROM book1 WHERE book_title like '% и %'