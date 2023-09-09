; поиск присутствия элемента в списке:
; берем каждый элемент списка (temp)
; и сравниванаем с элементом A
; если они равны, вернем T, иначе по окончанию nil
(defun search_element (a list_)
	(dolist (temp list_)
		(if (eq a temp) (return t))
	)
)

; пересечение множеств
(defun intersection_lists (a b)
	(setq result nil)
	(loop
		; если список A пустой, то возвращаем результат 
		(if (null a) (return result))
		; если голова списка A содержится в списке B, то добавляем ее к результату
		(if (search_element (car a) b) (setq result (append result (list (car a)))))
		; A = хвосту от A
		(setq a (cdr a))
	)
)