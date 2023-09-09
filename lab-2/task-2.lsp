;функция возведения числа в степень a^b
(defun pow (a b)
	(cond
		((= b 0) 1)
		(t (* a (pow a (- b 1))))
	)
)

(defun stairs (a)
	(cond
		;если список пустой => nil
		((null a) nil)
		;если один элемент => выведем этот элемент
		((null (cdr a)) (car a))
		;если остался 1 элемент, то возводим текущий элемент в степень
		((null (cddr a)) (pow (car a) (cadr a)))
		;возводим голову списка в степень
		(t (pow (car a) (stairs (cdr a))))
	)
)