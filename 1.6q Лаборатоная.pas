var 
  x: integer;
  digit1, digit2, digit3, digit4:integer;
 
  begin
    write('Введите четырехзначное число');
    readln(x);
    digit1:=x div 1000;
        digit2:=(x mod 1000) div 100;
            digit3:=(x mod 100) div 10;
                digit4:=x mod 10;
                if (digit1<digit2) and (digit2<digit3) and (digit3<digit4) then
                  write('true')
                else 
                  write('false')
  end.