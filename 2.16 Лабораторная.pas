var
  measurementunit: integer;
  L:real; 
  meters:real;
  begin
    write('Введите номер единицы измерения. 1-дециметр,2километр,3.метр,4 миллиметр,5 сантиметр');
    readln(measurementunit);
    write('Введите длину отрезка:');
    readln(L);
    case measurementunit of
      1:meters:= L / 10 ;
       2:meters:= L / 1000 ;
        3:meters:= L;
         4:meters:= L / 1000 ;
          5:meters:= L / 100 
          else
            write('Неверный номер единицы измерения');
          exit;
          end;
  writeln('Длина отрезка в метрах:' ,meters:4:2);
    end.
