
%{
   #include<stdio.h>
   int yylex(void);
   void yyerror(char* s);
%}
%token NUMBER
%left '+' '-'
%left '*' '/'

%%
S:E {printf("\nans is %d",$$);}
;
E: E'+'E {$$=$1+$3;}
   |E'-'E {$$=$1-$3;}
   |T {$$=$1;}
T: |T'*'F {$$=$1*$3;}
   |T'/'F {
      if($3==0)yyerror("divide by zero");
      else $$=$1/$3;
   }
F: |'('E')' {$$=($1);}
   |NUMBER {$$=$1;}
   ;
%%
int main(){
   yyparse();
}
int yywrap(){
   return 1;
}
void yyerror (char *s) {
   fprintf (stderr, "%s\n", s);
 }