var a,b,k:integer;
c,d: boolean;
begin
  a:=10;
  b:=20;
  c:=True;
  d:=False;
  k:=15;
 writeln('k mod 7=',k mod 7);
 writeln('k mod 5=',k mod 5);
 writeln('k mod 5-1=',k mod 5-1);
 if (k mod 7=k div 5-1) then
   write('Истина')
else 
  write('Ложь')
  
end.