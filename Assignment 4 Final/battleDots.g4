grammar battleDots;

start : expr | <EOF>;

expr 
    : name1=NAME? 'vs' name2=NAME #vsExpression
    | 'duration' time=INT '->' #durationExpression
    ;

INT : [1-9] [0-9]*;
NAME : [A-Za-z0-9]+;

WS : [ \r\n\t]+ -> skip;

