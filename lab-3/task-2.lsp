(defun inc_nums (a)
	(cond
		; если а - nil, то вернуть nil
		((null a) nil)
		; если число, то вернуть "число + 1"
		((numberp a) (+ 1 a))
		; если атом, вернуть атом
		((atom a) a)
		; собирать список из головы и хвоста, к которым применяем нашу функцию
		(t (cons (inc_nums(car a)) (inc_nums(cdr a))))
	)
)