```mermaid
flowchart TD
 Start([Начало]) --> InputQ[/Ввод параметров: Qж, W, M_min/]
 InputQ --> CheckValid{Qж в 0..1000 И W в 0..100?}
 CheckValid -- Нет --> InputQ
 CheckValid -- Да --> CalcVol[Расчёт объёма нефти: Qн = Qж * 1 - W/100]
 CalcVol --> CalcMass[Расчёт массы нефти: Mн = Qн * 850 / 1000]
 
 CalcMass --> CondStop{Mн == 0?}
 CondStop -- Да --> StatusStop[Статус: Скважина остановлена]
 CondStop -- Нет --> Cond1{Mн < 12.5?}
 
 Cond1 -- Да --> Status1[Статус: Убыточна - стоп]
 Cond1 -- Нет --> Cond2{Mн < 37.5?}
 Cond2 -- Да --> Status2[Статус: Рентабельна - база]
 Cond2 -- Нет --> Status3[Статус: Высокодебитная - приоритет]
 
 StatusStop --> Output[/Вывод: Qн, Mн, Статус/]
 Status1 --> Output
 Status2 --> Output
 Status3 --> Output
 Output --> End([Конец])
```
