domains
	list_int = integer*

predicates
	member(integer, list_int).
	intersection(list_int, list_int, list_int).

clauses
	member(X, [X|_]).
	member(X, [_|T]) :- member(X, T).

	/* пересечение пустого множества с любым множеством = пустое множество */
	intersection([], _, []). 

	/* если голова первого множества принадлежит второму множеству */
	/* то результатом будет множество, образованное головой первого */
	/* множества и хвостом, полученным пресечением хвоста первого множества со вторым множеством */

	intersection([Head|Tail_1], S2, [Head|Tail]):- member(Head, S2), intersection(Tail_1, S2, Tail).

	/* иначе результатом будет множество, полученное объединением */
	/* хвоста первого множества со вторым множеством */

	intersection([Head|Tail_1], S2, S):- not(member(Head, S2)), intersection(Tail_1, S2, S).