def caching_fibonacci():
    cache={}       # Сворюємо пустий словник, де будемо зберігати значення фібоначчі n, якщо його до цього не обчислювали
    
    def fibonacci(n):
        if n<=0:
            return 0
        elif n==1:
            return 1

        if n in cache:
            return cache[n]      # Якщо ми уже обчислювали потрібнне значення - функція бере його з кешу
        else: 
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)        #Якщо зачення немає ми рекурсивно обчислюємо доти, доки не зустрінемо відоме значенння
        return cache[n]
    return fibonacci     

fib = caching_fibonacci()


print(fib(10))  
print(fib(15))  