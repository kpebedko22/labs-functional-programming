# Лабораторная работа №1. Использование встроенных функций лиспа

## Задание №1

### Записать следующее выражения в виде s-выражений Лиспа.

```
(7.2-3.6)/(4*5-4.8)+3.6*5
```

```lisp
(+ (/ (- 7.2 3.6) (- (* 4 5) 4.8)) (* 3.6 5)) ⇒ 18.236842105263158
```

## Задание №2

### Определить, как будут выполнены интерпретатором Лиспа следующие последовательности s-выражений, т.е. что появится на выходе и какие значения получат символьные атомы в результате присваиваний.

```lisp
(SETQ A ‘C) ⇒ C
(SETQ B ‘A) ⇒ A
(SETQ B (SETQ B ‘C)) ⇒ C
```

## Задание №3

### Записать последовательность функций CAR и CDR, выделяющую из приведенных списков атом A.

```lisp
(1 2 ((3) A))

(CAR (CDR (CAR (CDR (CDR '(1 2 ((3) A))))))) ⇒ A
```

## Задание №4

### Каков результат интерпретации следующих выражений?

```lisp
(CAR (SET ‘A ‘(B C D))) ⇒ B
```

## Задание №5

### В данном упражнении требуется получить списки справа от стрелки с помощью суперпозиции функций LIST, APPEND, CONS, CAR, CDR. Аргументами функций могут быть лишь s-выражения, указанные слева от стрелки.

```
A; (B C); D ⇒ ((A) (B) C (D))
```

```lisp
(APPEND (LIST (LIST 'A) (LIST (CAR '(B C)))) (LIST (CAR (CDR '(B C))) (LIST 'D)))) ⇒ ((A) (B) C (D))
```

## Задание №6

### Какое из выражений дает значение T, а какое NIL?

```lisp
(NULL (NULL T)) ⇒ T
```

## Задание №7

### Чему равны значения следующих выражений?

```lisp
(OR (ATOM (< 5 3)) (SETQ C '8)) ⇒ T
```

## Задание №8

### Записать определения следующих функций, используя функции проверки условия IF и COND (т.е. 2 варианта!)

Функция, аргументом которой является числовой список, а результатом максимум из квадрата головы и суммы второго и третьего элементов.

```lisp
(DEFUN MAXL (A) 
    (IF (> (* (CAR A) (CAR A)) (+ (CADR A) (CADDR A)))
        (* (CAR A) (CAR A))
        (+ (CADR A) (CADDR A))
    )
)
```

```lisp
(DEFUN MAXL2 (A)
	(COND 
        ((> (* (CAR A) (CAR A)) (+ (CADR A) (CADDR A))) (* (CAR A) (CAR A)))
		(T (+ (CADR A) (CADDR A)))
	)
)
```
