var
  a,b:boolean;
  begin
    a:=True;
    b:=False;
    if(a and not b)or(not a and b)then
      write(' Истина')
    else
      write('Ложь')
  end.