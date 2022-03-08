grammar GCodes;

start : expr | <EOF>;

expr 
    : 'G01' x_cord=NUMBER y_cord=NUMBER #drawlineExpr
    | 'G28' #returnHomeExpr
    | 'Z' z_cord=NUMBER #heightExpr
    | 'print' x_cord=NUMBER y_cord=NUMBER #printlineExpr
    ;

NUMBER : '-'? ('0' .. '9')+ ('.' ('0' .. '9')+)?;

WS : [ \r\n\t]+ -> skip;

