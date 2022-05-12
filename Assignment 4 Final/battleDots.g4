grammar battleDots;

start : expr | <EOF>;

expr 
    : 'PLAYER' player_name=NAME #playerExpression
    | 'vs' #vsExpression
    | 'duration' seconds=INT #durationExpression
    ;

INT : [1-9] [0-9]*;
NAME : [A-Za-z0-9]+;

WS : [ \r\n\t]+ -> skip;

