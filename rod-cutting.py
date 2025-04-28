from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію
    """
    if length <= 0 or not prices or len(prices) != length:
        return {"max_profit": 0, "cuts": [], "number_of_cuts": 0}

    # memo[i] = (max_profit, cuts)
    memo = {}

    def helper(n):
        if n == 0:
            return 0, []
        if n in memo:
            return memo[n]
        max_val = float('-inf')
        best_cuts = []
        for i in range(1, n+1):
            profit = prices[i-1]
            rem_profit, rem_cuts = helper(n - i)
            if profit + rem_profit > max_val:
                max_val = profit + rem_profit
                best_cuts = [i] + rem_cuts
        memo[n] = (max_val, best_cuts)
        return memo[n]

    max_profit, cuts = helper(length)
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts)-1 if cuts else 0
    }


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію
    """
    if length <= 0 or not prices or len(prices) != length:
        return {"max_profit": 0, "cuts": [], "number_of_cuts": 0}

    dp = [0] * (length + 1)
    cut_choice = [0] * (length + 1)  # cut_choice[i] = перший розріз для довжини i

    for l in range(1, length + 1):
        max_val = float('-inf')
        for i in range(1, l + 1):
            if prices[i-1] + dp[l-i] > max_val:
                max_val = prices[i-1] + dp[l-i]
                cut_choice[l] = i
        dp[l] = max_val

    cuts = []
    n = length
    while n > 0:
        cuts.append(cut_choice[n])
        n -= cut_choice[n]

    cuts = cuts[::-1]

    return {
        "max_profit": dp[length],
        "cuts": cuts,
        "number_of_cuts": len(cuts)-1 if cuts else 0
    }

def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\n\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()