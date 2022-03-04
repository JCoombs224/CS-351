grammar turtle;

start: expr | <EOF>;

expr 
    : 'turtle' x_cord=NUMBER y_cord=NUMBER #drawlineExpr
    | 'print' x_cord=NUMBER y_cord=NUMBER #printlineExpr
    ;

NUMBER : ('0' .. '9') + ('.' ('0' .. '9')+)?;

WS : [ \r\n\t]+ -> skip;