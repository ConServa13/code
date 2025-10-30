
import os
import pandas as pd
import numpy as np
from tkinter import Tk, filedialog

def parse_input(input_str):
    try:
        # Разделяем строку на компоненты
        parts = input_str.split(':')
        if len(parts) != 2:
            return None, None, None
            
        # Проверяем формат x.y или x
        if '.' in parts[0]:
            coord = parts[0].split('.')
            if len(coord) != 2:
                return None, None, None
            x, y = coord
            value = parts[1].strip()
            return x, y, value
            
        # Проверяем формат x:value
        else:
            x = parts[0].strip()
            value = parts[1].strip()
            return x, None, value
            
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return None, None, None

def write_to_excel(df, x, y, value):
    try:
        # Преобразуем буквенное обозначение в номер столбца
        if x.isalpha():
            col = ord(x.upper()) - 65
        else:
            col = int(x) - 1
        if value.endswith('.int'):
            value = int(value[:-4])
        else:
            try:
                value = float(value)
            except ValueError:
                pass

            
        # Если указан номер строки
        if y:
            row = int(y) - 1
            df.iloc[row, col] = value
            
        # Если указан только столбец
        elif x.isalpha():
            # Пишем в следующую пустую ячейку столбца
            empty_row = df[df.iloc[:, col].isna()].index[0]
            df.iloc[empty_row, col] = value
            
        # Если указан только номер строки
        else:
            # Пишем через одну ячейку
            empty_col = df.columns[df.isna().iloc[int(x)-1]].tolist()
            if empty_col:
                df.iloc[int(x)-1, df.columns.get_loc(empty_col[0])] = value
            
        return df
    except Exception as e:
        print(f"Ошибка при записи в Excel: {e}")
        return df

def main():
    # Создаем окно для выбора файла
    root = Tk()
    root.withdraw()
    
    # Выбираем файл с данными
    file_path = filedialog.askopenfilename(
        title="Выберите файл с данными",
        filetypes=(("Text files", "*.txt"), ("all files", "*.*"))
    )
    
    # Выбираем файл для сохранения Excel
    save_path = filedialog.asksaveasfilename(
        title="Сохранить Excel файл как",
        defaultextension=".xlsx",
        filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*"))
    )
    
    # Создаем пустой DataFrame
    df = pd.DataFrame(np.nan, index=range(100), columns=list('ABCDEFGHIJ'))
    
    # Читаем данные из файла
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            x, y, value = parse_input(line)
            if x and value:
                df = write_to_excel(df, x, y, value)
                
    # Сохраняем в Excel
    df.to_excel(save_path, index=False, header=False)
    print(f"Файл успешно сохранен: {save_path}")

if __name__ == "__main__":
    main()
