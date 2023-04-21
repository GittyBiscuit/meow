%{
    int consonant = 0;
    int vowel = 0;
    int sentence = 0;
%}

%%
[aeiou] ++vowel;
[bcdfghjklmnpqrstvwxyz] ++consonant;
[.] ++sentence;
\n return 0;
%%


int yywrap(){}
int main(int argc, char **argv) {
    yylex();
    printf("\nnumber of consonants: %d\n", consonant);
    printf("\nnumber of vowels: %d\n", vowel);
    printf("\nnumber of sentences: %d\n", sentence);
    return 0;
}