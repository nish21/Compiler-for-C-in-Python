# Compiler-for-C-in-Python
Mini Project for Compiler Design course. A C compiler from scratch.

Handles while loops in C

Grammar

```
P -> STMTS

STMTS -> STMT STMTS | e

STMT -> while ( cond ) { STMTS }
      | Decl
      | Assign
      ;

Decl -> Type V;
V -> id V1
V1 -> , id | ;
Type -> int | float| char | long | short

Assign -> id = E;

C-> E0
E0-> E1E01
E01-> '||'E1E01 | e
E1-> E2E11
E11-> &&E2E11 | e
E2-> E3E21
E21-> >E3E21 | <E3E21 | e
E3-> E4E31
E31-> +E4E31 | -E4E31 | e
E4-> E5E41
E41-> *E5E41 | /E5E41 | e
E5-> (E) | id | num
```
