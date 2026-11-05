def calc_oil_volume(q_liq: float, w_pct: float) -> float:
    """Считает суточный объём чистой нефти по формуле: QH = Qж * (1 - W / 100)."""
    return q_liq * (1 - w_pct / 100)
 
def calc_oil_mass(q_oil: float, density: float = 850.0) -> float:
    return q_oil * density / 1000
 
def evaluate_profitability(m_oil: float, m_min: float) -> str:
    # Челлендж 2
    if m_oil == 0:
        return "Скважина остановлена (0 т/сут)"
    elif m_oil < m_min:
        return "Убыточна (стоп)"
    elif m_oil < 3 * m_min:
        return "Рентабельна (база)"
    else:
        return "Высокодебитная (приоритет)"
 
def get_valid_input(prompt: str, min_val: float, max_val: float) -> float:
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Ошибка: значение должно быть в диапазоне от {min_val} до {max_val}.")
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное число.")
 
if __name__ == "__main__":
    # Челлендж 1
    print("--- Проверка help() (Челлендж 1) ---")
    help(calc_oil_volume)
    print("-" * 40)

    print("--- Расчёт рентабельности скважины ---")
    
    q_liq = get_valid_input("Введите дебит жидкости Qж (м³/сут, 0–1000): ", 0, 1000)
    w_pct = get_valid_input("Введите обводнённость W (% , 0–100): ", 0, 100)
    m_min = get_valid_input("Введите порог рентабельности M_min (т/сут): ", 0, float('inf'))
    
    q_oil = calc_oil_volume(q_liq, w_pct)
    m_oil = calc_oil_mass(q_oil)
    status = evaluate_profitability(m_oil, m_min)
    
    print("\n--- Результаты расчёта ---")
    print(f"Объём чистой нефти (Qн): {q_oil:.2f} м³/сут")
    print(f"Масса нефти (Мн): {m_oil:.2f} т/сут")
    print(f"Статус скважины: {status}")
    print(f"(Проверка логики: M_min={m_min}, 3*M_min={3*m_min})")
