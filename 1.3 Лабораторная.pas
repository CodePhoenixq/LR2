var x, y: integer;
t,z, result: boolean;
begin
  x:=0;
  y:=2;
  t:=true;
  z:=false;
  result:= (x>=0) or (t and z) or (y*y<>4);
  writeln('Значение выражения', result)
end.