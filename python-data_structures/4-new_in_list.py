#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Əvvəlcə orijinal siyahının kopyasını yaradırıq
    copy_list = my_list[:]
    
    # İndeksi nüsxə üzərində yoxlayırıq
    if idx < 0 or idx >= len(my_list):
        return copy_list
    
    # Dəyişikliyi yalnız nüsxədə edirik
    copy_list[idx] = element
    return copy_list
