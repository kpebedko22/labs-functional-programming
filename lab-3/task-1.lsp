(defun get_last (a)
	(cond 
		; если a - атом, вернуть a
		((atom a) a)
		; если функция от хвоста возвращает nil,
		; то запускаем функцию от головы
		((null (get_last (cdr a))) (get_last (car a)))
		; иначе переходим к обработке хвоста
		(t (get_last (cdr a)))
	)
)