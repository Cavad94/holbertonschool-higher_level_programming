#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Modulun daxilindəki bütün adları götürürük
    names = dir(hidden_4)
    
    # Əlifba sırası ilə düzürük
    names.sort()
    
    for name in names:
        # Yalnız "__" ilə başlamayanları çap edirik
        if not name.startswith("__"):
            print(name)
