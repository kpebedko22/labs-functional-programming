; функция возведения числа в степень a^b
(defun pow (a b)
	(setq result 1)
	(dotimes (i (+ b 1)) 
		(if (= i b) (return result))
		(setq result (* result a)) 
	)
)

; функция возврата длины списка
(defun list_length (a)
	; если список пустой, вернем 0
	(if (null a) 0
		; иначе
		; инициализируем list_ списком A, result нулем
		; пока list_ не пустой, list_ становится хвостом текущего list_
		; result инкриментируется
		; если хвост list_ - пустой список, вернем (result + 1)
		(do ((list_ a (cdr list_)) (result 0 (+ result 1)))
			((null list_))
			(if (null (cdr list_)) (return (+ result 1)))
		)
	)
)

; функция возврата элемента по индексу 
; (первый элемент = 0, последний = длина списка - 1)
; лямбда функция возвращает "значение элемента + 1"
(defun get_element (list_ index)
	(setq j 0)
	; пройдемся по всем элементам списка
	; если j равняется index возвращаем элемент
	(dolist (temp list_)
		(if (eq j index) (return ((lambda (x) (+ x 1)) temp)))
		; инкриментируем j
		(setq j (+ j 1))
	)
)

; функция возведения элементов списка справа налево
(defun stairs (a)
	; res = 1
	; len = длина списка A
	(setq res 1)
	(setq len (list_length a))
	; с нуля до длины списка
	(dotimes (i len) 
		; если i равняется (длина списка - 1), т.е. работаем с элементом нулевого индекса
		; возвращаем этот элемент в степени res
		(if (= i (- len 1)) (return (pow (get_element a (- len i 1)) res)))
		; начинаем с последнего элемента списка, возводим его в степень res = 1
		; переходим к предпоследнему элементу списка, возводим его в степень res и т.д.
		(setq res (pow (get_element a (- len i 1)) res))
	)
)