mermaid
flowchart TD
Start([Начало]) --> InputQ[/Ввод параметров: Qж, W, M_min/]
InputQ --> CheckValid{Данные корректны?}
CheckValid -- Нет --> InputQ
CheckValid -- Да --> CalcVol [Расчёт объёма нефти: QH = Qж * 1 - W/100]
CalcVol --> CalcMass [Расчёт массы нефти: MH = QH * 850 / 1000]

CalcMass --> CondStop{MH == 0?}
CondStop -- Да --> StatusStop[Статус: Скважина остановлена]
CondStop -- Нет --> Cond1{MH < M_min?}

Cond1 -- Да --> Status1 [Статус: Убыточна стоп]
Cond1 -- Нет --> Cond2{MH < 3 * M_min?}
Cond2 -- Да --> Status2 [Статус: Рентабельна база]
Cond2 -- Нет --> Status3 [Статус: Высокодебитная приоритет]

StatusStop --> Output[/Вывод результатов на экран/]
Status1 --> Output
Status2 --> Output
Status3 --> Output
Output --> End([Конец])