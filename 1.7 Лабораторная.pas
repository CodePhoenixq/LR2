var
  x: real;
  t: boolean;
  begin
    write ('Введите координату x:');
    readln(x);
    t:=(x < -5) or (x>5) and (x < 10) or (x > 15);
    if t then 
      write('true')
    else
      write('false');
  end.