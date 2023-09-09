(defun search_element (a list)
	(cond
		;проверяем список на пустоту
		((null list) nil)
		;элемент принадлежит списку - вернуть T
		((eq a (car list)) t)
		;продолжаем проверку
		(t (search_element a (cdr list)))
	)
)

(defun intersection (a b)
	(cond
		;список a пуст
		((null a) nil)
		;список b пуст
		((null b) nil)
		;если голова a содержится в b, добавляем ее в ответ и продолжаем поиск
		((search_element (car a) b) (cons (car a) (intersection (cdr a) b)))
		;продолжаем поиск
		(t (intersection (cdr a) b))
	)
)