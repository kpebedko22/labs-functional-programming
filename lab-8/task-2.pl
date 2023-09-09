domains
	list_int = integer*

predicates
	pow(integer, integer, integer).
	stairs(list_int, integer).

clauses

	/* возведение в степень */
	pow(_, 0, Z):- Z = 1.
	pow(X, Y, Z):- Y > 0, Y_ = Y - 1, pow(X, Y_, Z_), Z = Z_ * X.

	/* если на вход поступил список из одного элемента */
	/* то ответ - сам элемент */
	stairs([Head | []], X):- X = Head.

	/* рекурсивно идем до конца списка и собираем степень */
	stairs([Head | Tail], X):- stairs(Tail, K), pow(Head, K, G), X = G.